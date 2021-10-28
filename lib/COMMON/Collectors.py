'''
This is microMG, MG = message, go!
'''

import socket
import network

from lib.COMMON.timer import Timer
from machine import Pin
from machine import reset
from lib.COMMON.TCPUPD import return_conn,TCP,UDP

sta = network.WLAN( network.STA_IF )
sta.active( 1 )

class collector():
    def __init__(self, apparatus,
                 H_CH='', HSlen=10, askShip=1, Hint=0): #h_CH=1...5
        # program start
        if Hint==1:
            from lib.COMMON.Hint_collector import OUT
        else:
            from lib.COMMON.Hint_collector import out as OUT
        self.OUT = OUT
        # self.Slot=Slot
        if HSlen == 'car':
            HSlen = 7
        if askShip==1:
            self.Ship=1
        else:
            self.Ship = 0
        import time
        self.randomDelay_askship = time.ticks_us() % 1000
        # if self.Slot==1:
        try:
            self.slotToGPIO={}
            self.btnToGPIO={}
            for i in range(1, apparatus.SlotTotal + 1):
                self.slotToGPIO.update( {i: Pin( apparatus.__dict__.get( 'Slot' + str( i ) ), mode=Pin.OUT )} )
            # SWITCH
            from lib.ASSEMBLE.GPIO.Switch import switch
            self.switch = switch( self.slotToGPIO )
        # try:
            apparatus.BtnTotal
            for i in range(1, apparatus.BtnTotal + 1):
                self.btnToGPIO.update( {i: Pin( apparatus.__dict__.get( 'Btn' + str( i ) ),mode=Pin.IN,pull=Pin.PULL_UP)} )
            from lib.ASSEMBLE.Button.Btn import Button
            self.btn = Button (self.btnToGPIO, self.slotToGPIO)
        except:
            print ('initial slot btn error')
        self.switchlen = 21
        self.assign_port = 700
        self.H_port = [801, 802, 803, 804, 805]
        # self.competition_port = 900
        self.regular_port = 1000
        self.H_failCount = 0
        # self.LData_len = Ldatalen # I DON'T USE THIS YET.
        self.HdataLen_str = '%04d' % HSlen
        self.Hcheck = ''.join(['*' for i in range(HSlen)])
        self.shakeData_len = 6
        self.OfflineCount = 0
        self.isHighSpeed = 0
        self.isHalfduplex_recv = 1
        # self.Latest_Hdata=None
        self.RunAfter = Timer.RunAfter
        # self.isSendRepeat=isSendRepeat
        self.counter = 0
        self.ssid=apparatus.ssid
        self.passwd=apparatus.passwd
        self.name=apparatus.__name__
        self.UDP_LS=UDP()
        self.TCP_1=TCP()
        self.TCP_2=TCP()
        self.sentData= ''


        def connectwifi(station, ssid, password, H_CH, recv=''):
            station.disconnect()
            station.connect(ssid, password)
            while station.isconnected() == 0 and self.counter <= 5:
                self.OUT(1)
                Timer.delayMS(5000)
                self.counter += 1
            # assigned for ID
            if H_CH != '':
                self.OUT(2)
                self.highSpeed_port = self.H_port[H_CH - 1]
                s = 'H' + str(H_CH - 1)
            else:  # LOW SPEED SHAKEDATA
                self.OUT(4)
                s = 'L_'
            # while station.isconnected() == 1 and recv[-2:]!='__': # ask ID from ship
            while recv[-2:] != '__':  # ask ID from ship
                recv = self.TCP_1.send('0000' + s + self.name, self.assign_port)
                if recv=='NAME USED':
                    reset()

            self.ID = recv[:4]
            self.shakeData = self.ID + s
            self.OUT(5,recv)

        # connect to WIFI , then socket
        if sta.isconnected() == 0:
            # sta.ifconfig( (apparatus.IPprefix + str( apparatus.ID ), '255.255.255.0', apparatus.IPprefix + '1', apparatus.IPprefix + '1') ) # manually assign IP addr, but No ID in management.py, so cancel.
            connectwifi(sta, self.ssid, self.passwd,H_CH)
        else:
            self.OUT(6)

        # IF HIGH SPEED, send data to ship right now. However, low speed needn't send data to ship now.
        # How about that, low speed send data too.
        if H_CH != '' and self.ID!='':
            recvData = self.TCP_1.send(self.HdataLen_str, 8000)
            del (self.HdataLen_str)
            if recvData == 'OK':
                self.OUT(7,str( self.highSpeed_port ))
                self.H_clientSocket = return_conn(int(self.highSpeed_port))
                if self.H_clientSocket != 1:
                    self.isHighSpeed = 1
                    self.H_clientSocket.settimeout( 0.1 )
                else:
                    self.OUT(8)
                # conn.close()
            elif recvData == 'CH USED':
                self.OUT(9)
                Timer.delayMS(5000)
                reset()
            else:
                self.OUT(10)
                Timer.delayMS(5000)
                reset()

    def askAssist(self,str): # api
        # name,cmd=cmd.split('!') old way
        cmd,name=str.split('@')
        if name=='self':
            self.switch.GetRawCMD(cmd)
        elif '@' not in name:
            # self.send('Assist'+name+'!'+cmd) # send it as low speed old way
            self.send('Assist'+cmd+'@'+name) # send it as low speed
        else:
            self.OUT(21)

    def remoteLink(self, btn, slot,name,locked=1): # api
        data= 'Btn'+','.join(str(i) for i in btn)+'Slot'+','.join(str(i) for i in slot)+'L'+str(locked)+'@'+name
        self.send(data) # send it as low speed

    def askShip(self,recvData = ''): # the unique channel of connect with ship
        # if self.RunAfter( self.name + '_' + str( 800 + self.randomDelay_askship)):
        if self.RunAfter( self.name ,  800 + self.randomDelay_askship):
            while recvData=='':
                if self.RunAfter('askship',450):
                    if self.OfflineCount > 7: # if can't recv data over 7times, send 'check' to server to prove not offline.
                        recvData = self.TCP_1.send(self.shakeData + 'check', self.regular_port, mode='halfduplex')
                    else:
                        recvData = self.TCP_1.send(self.shakeData + 'Slot', self.regular_port, mode='halfduplex')

            if recvData =='receiving':
                pass

            elif recvData in ( '_', 1):
                self.OfflineCount += 1
                self.OUT(12,self.OfflineCount)
                if self.OfflineCount > 15:
                    self.OUT(13)
                    reset()

            else:
                # self.askshipConn.close()
                if recvData == 'reassignID':
                    self.OUT(14)
                    reset()
                rawdata = recvData[self.shakeData_len:]
                self.OUT(15,recvData)

                if rawdata[:3]=='Btn' and 'Slot' in (rawdata): # For remote alter Link
                    print (111111111111,rawdata)
                    # B,S,L=rawdata.replace('Btn','').replace('Slot','').replace('_','')
                    B=rawdata.split('Slot')[0].replace('Btn','')
                    S, L = rawdata.split('Slot')[1].split('L')
                    Btn=B.split(',')
                    Slot=S.split(',')
                    self.btn.addlink(Btn,Slot,int(L))
                elif rawdata == 'check':
                    self.OfflineCount = 0
                    self.OUT(16)
                elif '*' in rawdata: # "*" appears, it means recv a CMD str, i can use '@' as well.
                    return rawdata  # Switch.py needs this, 'laser' is the old name which shows gpio on board, now, only for the laser sword
                    # else: # this may be never used
                    #     b = rawdata.split( ',' ) # "comma" means split two cmds, but "comma" may never has been used, it was the old way, delete this part? checked 1 time, it can be deleted.
                    #     for i in range( len( b ) ):
                    #         self.slotToGPIO[int( b[i].split( '-' )[0] )].value( int( b[i].split( '-' )[1] ) )

    def send(self, data, LS_interval=1000, recvData='_', repeatable=0): # api
        if repeatable==1:
            pass
        elif data == self.sentData:
            return
        if LS_interval<500:
            LS_interval=500
        if self.isHighSpeed:
            if self.RunAfter(self.name ,50):
                try:
                    self.H_clientSocket.send(data.encode())
                    self.H_failCount = 0
                    if self.RunAfter(self.name + 'HC',14000):
                        self.H_clientSocket.send(self.Hcheck)
                    self.sentData = data
                except:
                    Timer.delayMS(700)
                    self.H_failCount += 1
                    self.OUT(17)
                    if self.H_failCount > 8:
                        for i in reversed(range(1,6)):
                            Timer.delayMS(1000)
                            self.OUT(18)
                        reset()  # for moment when officially start to use
        else: # Low speed and assisting here
            if Timer.RunAfter( 'LSdefault' ,LS_interval):
                while recvData=='_':
                    self.OUT(19,(self.shakeData , data))
                    recvData=self.TCP_2.send(self.shakeData + data, self.regular_port)
                    self.sentData = data
                    print ('sent to regular_port: ', self.shakeData + data)
                if recvData=='reassignID':
                    self.OUT(20)
                    reset()

    def Main(self):
        if self.Ship:
            self.switch.GetRawCMD(self.askShip())
        self.btn.link()



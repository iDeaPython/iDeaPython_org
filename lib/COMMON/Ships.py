import socket
import time
import network
from lib.COMMON.timer import Timer
from machine import Pin

class ship():
    def __init__(self, Host, Hint=0, Ldata_len=32, Slot=1):
        ap = network.WLAN(network.AP_IF)  # create AP interface
        ap.active(1)  # activate the interface
        ap.config( essid=Host.ssid, password=Host.passwd, authmode=4, channel=9 ,max_clients=10 )  # set the ESSID of the access point
        time.sleep_ms(3000)
        if Hint==1:
            from lib.COMMON.Hint_ship import OUT 
        else:
            from lib.COMMON.Hint_ship import out as OUT
        self.OUT=OUT
        self.assign_port = 700
        # self.competition_port = 900
        self.regular_port = 1000
        # self.competition_users_num = 0
        self.ID_socket = socket.socket()  # get instance
        self.ID_socket.bind(('0.0.0.0', self.assign_port))  # bind host address and port together
        self.ID_socket.listen(5)
        self.ID_socket.settimeout(0)

        self.regular_socket = socket.socket()  # get instance
        self.regular_socket.bind(('0.0.0.0', self.regular_port))  # bind host address and port together
        self.regular_socket.listen(5)
        self.regular_socket.settimeout(0)
        self.Ldata_len = Ldata_len
        self.Hdata_str = None
        self.used_ch=[]
        # self.Ldata_str = None
        self.shakeData_len = 6
        # self.compRecv_len = 1
        self.recv_List = []
        self.isHighSpeed = [0, 0, 0, 0, 0]
        self.H_conn = ['H_conn0', 'H_conn1', 'H_conn2', 'H_conn3', 'H_conn4']
        self.H_checkOnline = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        self.H_socket = {'H_socket0': 801, 'H_socket1': 802, 'H_socket2': 803, 'H_socket3': 804, 'H_socket4': 805}
        self.isGet_H = 0
        # self.shakeToLData_dict = {}  # i don't remember, but it may be only for competition.
        self.switch_dict = {}
        self.linkAlterList={}
        # self.storeID = {}
        self.onlineLS_ID = {}
        self.offList=[]
        self.name_id={'Ship':'0000'}
        # self.isSendSwitch = {}
        # Timer.init() # run in boot.py
        self.RunAfter = Timer.RunAfter
        if Slot==1:
            self.slotToGPIO={}
            self.btnToGPIO={}
            for i in range(1, Host.SlotTotal + 1):
                self.slotToGPIO.update( {i: Pin( Host.__dict__.get( 'Slot' + str( i ) ), mode=Pin.OUT )} )
            # SWITCH
            from lib.ASSEMBLE.GPIO.Switch import switch
            self.switch = switch( self.slotToGPIO )
            # now you can use API from switch.py

        try:
            Host.BtnTotal
            for i in range(1, Host.BtnTotal + 1):
                self.btnToGPIO.update( {i: Pin( Host.__dict__.get( 'Btn' + str( i ) ),mode=Pin.IN,pull=Pin.PULL_UP)} )
            from lib.ASSEMBLE.Button.Btn import Button
            self.btn = Button (self.btnToGPIO, self.slotToGPIO)
        except:
            pass

    # def varName_manage(self, name):
    #     return getattr( __import__( 'lib.COMMON.management', globals(), locals(), [name, ], 0 ), name )

    def updateSwitch(self, name, cmd):   # api
        # self.switch_dict['%04d' % apparatus.ID] = [CMD.strip(), True]
        try:
            self.switch_dict[self.name_id[name]] = [cmd.strip(), True] # True means avalivable to update, false means has updated, won't send the update switch data to collector again.
            self.OUT(1, (self.name_id[name], name))
        except:
            print (name, '\n has not connected yet\n')


    # def assistFire(self,name,cmd):
    #     self.updateSwitch(name, cmd)

    def try_connAccept(self, conn1, time=0):
        try:
            conn, addr = conn1.accept()
            conn.settimeout(time)
            return conn,1
        except:
            pass
        return None,0

    def wait_newconn(self,shakeData=''):
        if self.RunAfter('newConn',1100):
            conn,y = self.try_connAccept(self.ID_socket, 0.5)
            if y==1: # To assign ID
                shakeData = conn.recv(20).decode()
                if shakeData[:4] == '0000':
                    # ID=self.assignID()
                    # self.OUT(2,ID)
                    # self._send_data(conn, ID + '__')
                    # conn.close()
                    try:
                        self.name_id[shakeData[6:]] # check exsit or not
                        print ('NAME REGISTERED ON SHIP, reject!')
                        self._send_data(conn, 'NAME USED')
                        return
                    except:
                        ID = self.assignID()
                        self.OUT(2, ID)
                        self._send_data(conn, ID + '__')
                        conn.close()
                        self.name_id[shakeData[6:]] = ID
                        print ('\nA new collector: ',shakeData[6:],'\n')
                    shakeData = ID + shakeData[4:6]
                conn.close()
            else:
                return
            self.OUT(3,shakeData)
            if shakeData[0] != '_':
                # Add into list
                # USAGE: constantly use client, it needs to start after the previous one has been settled down.
                if shakeData[-2:-1] == 'H':
                    i = int(shakeData[-1:])  # i is the number of channel

                    # STEP ONE, create socket in port 8000 to receive length of H_data
                    socketLength = socket.socket()
                    # print( 111111111 )
                    socketLength.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                    socketLength.bind(('0.0.0.0', 8000))
                    # print( 222222222 )
                    socketLength.listen(5)
                    socketLength.settimeout(10)
                    connLength,y = self.try_connAccept(socketLength)
                    if y != 0:
                        connLength.settimeout(5)  # keep 5s, very important before create high speed connection.
                        recv = self._recv_data(connLength, 4)
                        # print( 3333333333 )
                        self.OUT(4,recv)
                        # send length back
                        if recv != '_':
                            self.Hdata_len = int(recv)
                            if i not in self.used_ch:
                                self._send_data(connLength, 'OK')
                            else:
                                self._send_data(connLength, 'CH USED')
                                connLength.close()
                                socketLength.close()
                                self.OUT(5)
                                return
                        else:
                            self.OUT(6)
                            return
                    else:
                        self.OUT(7)
                        pass

                    # STEP TWO, create socket in port(800...804) to receive H_data as such
                    if connLength != 0:
                        H_socket = list(sorted(self.H_socket.keys()))[i]  # get data from position 0
                        globals()[H_socket] = socket.socket()  # this line must after try.
                        globals()[H_socket].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                        globals()[H_socket].bind(
                            ('0.0.0.0', self.H_socket[H_socket]))  # bind host address and port together
                        globals()[H_socket].listen(5)
                        globals()[H_socket].settimeout(5)
                        self.OUT(8,(self.H_socket,H_socket))
                        globals()[self.H_conn[i]],y = self.try_connAccept(globals()[H_socket])
                        if y != 0:
                            globals()[self.H_conn[i]].settimeout(0.05)
                            self.isGet_H = 1
                            self.isHighSpeed[i] = 1
                            self.OUT(9)
                            connLength.close()
                            socketLength.close()
                        else:
                            self.OUT(10, str(i))
                        self.used_ch.append(i)

    def _send_data(self, conn, str):
        conn.send(str.encode())

    def assignID(self):
        for i in range(len(self.onlineLS_ID)+1):
            i += 1
            try:
                self.onlineLS_ID.__getitem__('%04d' % i)
            except:
                # self.onlineLS_ID['%04d' % i] = i
                self.onlineLS_ID['%04d' % i] = 0 # the init status is 0
                return '%04d' % i

    def _recv_data(self, conn, length):
        # self.connAccept = conn
        recv = '_'
        if length == self.shakeData_len or length == 4:
            recv = conn.recv(length).decode()
        else: # only use for get_L
            try:
                self.conn = conn.accept()[0]
                # self.connAccept,addr = self.conn.accept()
                self.conn.settimeout(0.1)
                recv = self.conn.recv(length).decode()
            except:
                pass
        return recv

    def _get_L(self):
        recv = self._recv_data(self.regular_socket, self.shakeData_len + self.Ldata_len)  # recv has included accept()
        if recv != '_':
            shakedata = recv[:self.shakeData_len]
            uniqueid = shakedata[:4]
            rawdata = recv[self.shakeData_len:]
            print('\n\nrecv after ID:', rawdata[:6])
            if uniqueid not in self.onlineLS_ID:
                self._send_data(self.conn, 'reassignID') # make collector reboot
                self.conn.close()
                self.OUT(12)
                return
            self.onlineLS_ID[uniqueid] += 1
            try:
                self.offList.remove(uniqueid)
            except :
                pass
            self.OUT(13,(rawdata,shakedata))

            # need to send link?
            if uniqueid in self.linkAlterList:
                self._send_data(self.conn, shakedata + self.linkAlterList[uniqueid])
                del self.linkAlterList[uniqueid]

            # for remote alter Link
            if rawdata[:3] == 'Btn':
                data, name = rawdata.split('@')
                self.OUT(15,name)
                # self.linkAlterList['%04d' % self.getNameFromID(name).ID] = data
                self.linkAlterList[self.name_id[name]] = data

            # for sending switch_dict to collectors
            elif rawdata[:4] == 'Slot':
                try: # check the id in switch_dict
                    a = self.switch_dict[uniqueid][1] # [1] means available to update ,[0] means the cmd string.
                    self.OUT(16,(uniqueid,a))
                except:
                    self.OUT(17,(uniqueid))
                    a = 0
                if a:
                    self._send_data(self.conn, shakedata + self.switch_dict[uniqueid][0]) # [0] means the cmd string, [1] means avaliable to update
                    self.switch_dict[uniqueid][1] = False
                    self.OUT(18,(shakedata,self.switch_dict[uniqueid][0]))

            # for assist, just change the data in dict of switch_dict, no sending here.
            elif rawdata[:6] == 'Assist':
                print ('\nship got an assistant command\n')
                str1 = rawdata[6:]
                cmd,name=str1.split('@')
                # self.assistFire(name, cmd)
                self.updateSwitch(name, cmd)
                self.OUT(14)

            elif rawdata == 'check':
                self._send_data(self.conn, shakedata + 'check')

            else: # custom LS data, problem, why LS, not L data
                self.Ldata= uniqueid, rawdata
            self.conn.close()
            self.OUT(19)

    def _get_H(self, i, conn):
        try:
            recv = conn.recv(self.Hdata_len).decode()  # don't use _recv_data()
        except:
            recv = '_'
        if recv == '_':
            self.Hdata_str = None
            self.H_checkOnline[i] += 1
            # accumulation greater than 200
            if self.H_checkOnline[i] > 100:  # 100 = about 10s
                self.isHighSpeed[i] = 0
                self.H_checkOnline[i] = 0
                conn.close()  # close accept
                globals()[list(sorted(self.H_socket.keys()))[i]].close()  # close socket
                self.OUT(20,str(i))
                self.OUT(21,list(sorted(self.H_socket.keys()))[i])
                del (globals()[self.H_conn[i]])
                self.OUT(22,self.H_conn[i])
                del (globals()[list(sorted(self.H_socket.keys()))[i]])
                self.used_ch.remove(i)
                self.Hdata_str = 'offline'
        else:
            self.H_checkOnline[i] = 0
            self.Hdata_str = recv if '*' not in recv else None
            self.OUT(23,self.Hdata_str)

    def start_server(self):
        if self.isGet_H and self.RunAfter('HS',50):
            for i in range(5):
                if self.isHighSpeed[i]:
                    self._get_H(i, globals()[self.H_conn[i]])
        if self.RunAfter('lowSpeed',350):
            self._get_L()

    def Main(self):  # put it into "while" statement
        list1 = []
        self.wait_newconn()
        self.start_server()
        if Timer.RunAfter('CheckOL',20000): # sentry
            self.OUT(24,self.onlineLS_ID)

            for ID in self.onlineLS_ID.keys():
                list1.append(ID)
            for ID in list1:
                if self.onlineLS_ID[ID] == 0 : # online times=0
                    if ID in self.offList: # delete offline ID and name
                        self.offList.remove(ID)
                        self.onlineLS_ID.pop( ID )
                        del self.name_id[[key for key, value in self.name_id.items() if value == ID][0]]
                        self.OUT(25,ID)
                    else:
                        self.offList.append(ID)
                        self.OUT(26,self.offList)
            self.onlineLS_ID=dict.fromkeys(self.onlineLS_ID,0)


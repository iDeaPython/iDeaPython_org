from lib.COMMON.timer import Timer

class switch( object ):
    def __init__(self,slotToGPIO):
        # self.conn = conn
        self.CMDing = 0
        self.lastMSG=''
        self.RunAfter = Timer.RunAfter
        self.slotToGPIO=slotToGPIO
        self.lastRawCMD=None
        # self.setgpio = lambda b,bool: slotToGPIO[int(b)].value( bool )
        # self.setSLOTdata=None

    def setSlot(self, s, Bool): # api

        # if s!=self.setSLOTdata:
        try:
            self.slotToGPIO[int(s)].value(Bool)
            # self.setSLOTdata=s
        except :
            pass
    def setstatus(self,i): # Change the status of the list of self.Slots.
        # for s in self.slots[i]:
        #     if self.simpleCMD:
        #         print ('this a simple command, self.rounds(on/off): ',self.rounds[i])
        #         # self.setSlot(j, self.rounds[i]) # when simpleCMD, self.rounds stored on/off
        #         self.setSlot(s, self.rounds[0]) # when simpleCMD, self.rounds stored on/off
        #     else:
        #         self.setSlot(s, self.status[i])
        if self.simpleCMD:
            # print('this a simple command, self.rounds(on/off): ', self.rounds[0])
            # print('setSlot: ', self.slots[i])
            # self.setSlot(j, self.rounds[i]) # when simpleCMD, self.rounds stored on/off
            self.setSlot(self.slots[i], self.rounds[0])  # when simpleCMD, self.rounds stored on/off
        else:
            self.setSlot(self.slots[i], self.status[i])
            # print('SET STATUS IS ', self.status[i])

    def MSG(self, data=None):
        if self.CMDing:     # While in process of CMDing, can receive new data, but can't deal with it
            for i in range( len( self.slots ) ):

                if self.simpleCMD: # means only on/off

                    self.setstatus(i)
                    self.CMDing = 0
                # elif self.simpleCMD==0 and self.rounds[i]>0:
                elif self.rounds[i]>0:
                    # k,l= self.interval[i].split('_')
                    # o = k+'_5256000' if int(l)==0 else k+'_'+l # 5256000 mean 10 years
                    if self.RunAfter(self.interval[i][0], self.interval[i][1]):
                        # print('CHANGE status of slot')
                        self.status[i] = not self.status[i]
                        self.setstatus(i)
                        if self.status[i]==0: # when status is OFF, rounds - 1 ??
                            self.rounds[i] -= 1
                        if self.rounds[i] == 0:
                            self.setstatus(i)
                            self.countTimes -= 1
                            # print( '\ncountTimes -1 \n' )
                            if self.countTimes==0:
                                self.CMDing = 0
                                print( '\nDone! You can receive data\n' )

        elif data!=None: # Analyze the data, for CMDing in the next round
            self.slots, self.interval, self.rounds, self.status,  = [], [], [], []
            # print ('data:',data)
            # Data = data.split(',')
            # for i in range(len(Data)): # this can be abandoned, it's for all commands in one, but now, just send one. not test yet.
            # aa = Data[i].split('*')[0]
            slots = data.split('*')[0]
            print ('1, data:',data)
            # if '_' in aa:   # When it has more than one slot(not gpio)
            #     for j in aa.split('_'):
            #         self.slots.append(j)
            #         self.countTimes = len(self.slots)
            #         self.status.append(True)  # Each of status of switch is ON initially
            #         self.setSlot(j, True) # Set slot high by initial
            #         self.interval.append(('MSG'+str(j), int(data.split('*')[1].split('-')[0]) * 1000))
            #         self.rounds.append(int(data.split('*')[1].split('-')[1]))
            #
            #     # self.slots.append( b2 )
            # else:   # When it has ONLY ONE SLOT
            #     self.setSlot(aa, True) # Set slot high by initial
            #     self.slots.append( aa )
            #     self.status.append(True)  # Each of status of switch is ON initially
            #     self.interval.append(('MSG1', int(data.split('*')[1].split('-')[0]) * 1000))
            #     self.rounds.append(int(data.split('*')[1].split('-')[1]))

            if '_' in slots:  # When it has more than one slot(not gpio)
                i=slots.split('_')
            else:   # When it has ONLY ONE SLOT
                i=slots
            for j in i:
                self.slots.append(j)
                self.status.append(True)  # Each of status of switch is ON initially
                self.setSlot(j, True)  # Set slot high by initial
                self.interval.append(('MSG' + str(j), int(data.split('*')[1].split('-')[0]) * 1000))
                self.rounds.append(int(data.split('*')[1].split('-')[1]))
            self.countTimes = len(self.slots)

            if int(data.split('*')[1].split( '-' )[0])==0:
                print('3, this is a simpleCMD')
                self.simpleCMD=1
            else:
                print('3, this is not a simpleCMD')
                self.simpleCMD=0

            print('\nself.slots:', self.slots)
            print('\nself.rounds:', self.rounds)
            print('\nself.status:', self.status)
            print('\nself.interval:', self.interval)
            print('\nself.countTimes:', self.countTimes)
            self.CMDing = 1

    def GetRawCMD(self, RawCMD):
        if RawCMD not in (None,self.lastRawCMD):
        # if self.CMDing or RawCMD!=None : # Why use "or ", not "and"
            # print (self.lastMSG,switchMSG)
            # if RawCMD!=None:
            self.CMDing = 0 # When CMDing = 0, it will analyse RawCMD, Why did i put it here? oh, to make sure if i recv a new cmd, it will update a cmding which is running!
            self.MSG(RawCMD)
            self.lastRawCMD = RawCMD
            print ('4, finished analyse CMDdata')
        elif self.CMDing:
            self.MSG()



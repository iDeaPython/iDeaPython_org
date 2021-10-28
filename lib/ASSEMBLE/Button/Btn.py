from lib.COMMON.timer import Timer
# from machine import Pin


class Button(object):  # using timer
    def __init__(self, btnToGPIO, slotToGPIO, sec=0.5):
        self.RunAfter = Timer.RunAfter
        self.btnToGPIO = btnToGPIO
        self.slotToGPIO = slotToGPIO
        # self.BtnList = BtnList
        # self.SlotList = SlotList
        self.sec = sec
        self.dict1 = {}
        # self.setgpio = lambda b,bool: btnToGPIO[int(b)].value( bool )
        self.down = None
        self.BtnSlot=[]
        self.BTNstatus=0
        self.pressing=0
    def addlink(self,list1,list2,locked=1): # API
        self.BtnSlot.append([list1,list2,locked])


    def link(self):
        if Timer.RunAfter('link', 200) and self.BtnSlot!=[]:
            for j in self.BtnSlot:
                BtnList=j[0]
                SlotList=j[1]
                locked=j[2]
                # if self.Pressed( BtnList ) and self.RunAfter('btn' + ''.join([str(i) for i in BtnList]) + '_' + str(int(self.sec * 1000))):
                if self.Pressed( BtnList ):
                    # print ('pressed')
                    self.dict1 = {}
                    if locked:
                        if self.pressing==0:
                            for i in SlotList:
                                #run this one time until self.down =0
                                self.slotToGPIO[int(i)].value(not self.slotToGPIO[int(i)].value())
                            self.pressing=1

                    else:
                        for i in SlotList:
                            self.slotToGPIO[int(i)].value(1)
                else:
                    # print('button up')
                    self.pressing = 0
                    if locked==0:
                        for i in SlotList:
                            self.slotToGPIO[int(i)].value(0)
# when btn up (value=1), it can check next status.
    def Pressed(self, BtnList): # api, When the GPIO connects to GND, it means pressed.
        if Timer.RunAfter('pressed_', 200):
            len1 = len( BtnList )
            if len1 >= 2 and self.sec == 0.5: # if more than one button need to be pressed, then set sec during pressing at one sec
                self.sec = 1
            for i in BtnList:
                if self.btnToGPIO[int(i)].value() == 0:
                    self.dict1[int(i)] = self.btnToGPIO[int(i)]
                    self.down = 1
                elif self.btnToGPIO[int(i)].value() == 1:
                    self.down = 0

            if self.down == 1 and len(self.dict1) == len1:
                self.BTNstatus = 1
            else:
                self.BTNstatus = 0

        return self.BTNstatus


'''
issus:
1. link can't repeatedly run
2. gpio should be go "switch on/off", solved?
'''

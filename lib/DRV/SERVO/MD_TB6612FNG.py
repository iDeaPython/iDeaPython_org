from machine import PWM,Pin
from lib.COMMON.Arduino import Arduino_func

class Motor(): # compatible with DRV8833

    # d6-gpio12, d7-gpio13 for motorA, d2-gpio4 as PWMA
    # d5-gpio14, d8-gpio15 for motorB. NO SUFFICIENT GPIO, use PWMA.
    def __init__(self, in1=12, in2=13, in3=14, in4=15, pwm=4, motor_double=False,motor_directional=False, Min_Level=0, Max_Level=10, Min_duty=0,
                 Max_duty=1023):
        self.DOUBLEMOTOR = False
        self.DOUBLEMOTOR_DIRECTIONAL = False
        self.PWMA = PWM( Pin( pwm ), freq=50 )
        self.MOTORA = {'out1': Pin( in1, Pin.OUT ), 'out2': Pin( in2, Pin.OUT )}
        self.Min_Move_Level = Min_Level
        self.Max_Move_Level = Max_Level
        self.Min_DUTY = Min_duty
        self.Max_DUTY = Max_duty
        self.FWvalue,self.BWvalue=None,None
        if motor_double=='Double':
            if motor_directional == 1:
                self.DOUBLEMOTOR = True
            else:
                self.DOUBLEMOTOR_DIRECTIONAL = True
            self.MOTORB = {'out1': Pin( in3, Pin.OUT ), 'out2': Pin( in4, Pin.OUT )}

    def motorSpin(self, motor,num):
        if num == 1:
            motor['out1'].value( 1 )
            motor['out2'].value( 0 )
        elif num == 0:
            motor['out1'].value( 0 )
            motor['out2'].value( 1 )

    def v2d(self,value): # value of duty to decimal
        arduino_map = Arduino_func( self.Min_Move_Level, self.Max_Move_Level, self.Min_DUTY, self.Max_DUTY )
        value = arduino_map.map( value )
        return value

    def forward(self, value): # change this, if value didn't change, do run it.
        if value!=self.FWvalue:
            self.PWMA.duty( self.v2d(value) )
            self.motorSpin( self.MOTORA,1 )
            if self.DOUBLEMOTOR:
                self.motorSpin(self.MOTORB, 1 )
            self.FWvalue=value
    def backward(self, value): # change this, if value didn't change, do run it.
        if value != self.BWvalue:
            self.PWMA.duty( self.v2d(value) )
            self.motorSpin(self.MOTORA, 0 )
            if self.DOUBLEMOTOR:
                self.motorSpin(self.MOTORB, 0 )
            self.BWvalue = value
    # ONLY FOR DOUBLE MOTORS, motorA = left side wheels, motorB = right side wheels
    def motor_turnleft(self, value):
        self.PWMA.duty( value )
        if self.DOUBLEMOTOR_DIRECTIONAL:
            self.motorSpin(self.MOTORA, 0 )
            self.motorSpin(self.MOTORB, 1 )

    def motor_turnright(self, value):
        self.PWMA.duty( value )
        if self.DOUBLEMOTOR_DIRECTIONAL:
            self.motorSpin(self.MOTORA, 1 )
            self.motorSpin(self.MOTORB, 0 )


    def move(self, value):
        move_value = list( value )
        move_value.pop( 0 )
        move_value = int( ''.join( move_value ) )
        if value[0] == 'F':
            self.forward( move_value )
        elif value[0] == 'B':
            self.backward( move_value )
        # print('move_value' + str(move_value))


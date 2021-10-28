from lib.DRV.SERVO.MD_TB6612FNG import Motor # compatible with DRV8833
# Default: motorA in1=GPIO 12, motorA in2=GPIO 13, motorB in1=GPIO 14, motorB in2=GPIO 15, pwm=GPIO 4, type='Single'(can be type='Double')
motorDriver = Motor()
# basic function

motorDriver.motorSpin(motorDriver.MOTORA, 1) # motorA spin clockwise
motorDriver.motorSpin(motorDriver.MOTORA, 0) # motorA spin count-clockwise

# advnaced function
motorDriver.forward(1) # speed is 1
motorDriver.forward(10) # speed is 10(max)
motorDriver.backward(10) # speed is 10(max)

# ONLY FOR DOUBLE MOTORS, motorA is on the left side wheels, motorB is on the right side wheels
motorDriver.motor_turnleft(1) # the turning speed from 1 to 10

# self-define
motorDriver.move('F01') # forward at speed 1
motorDriver.move('B01') # backward at speed 1

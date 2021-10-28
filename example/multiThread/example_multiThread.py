from lib.COMMON.timer import Timer

a1='test_3000'
a2='test_2000'
a3='test_1000'
a4='test_100'
# THE VAR IN RunAfter CAN NOT BE REPEATEDLY USE
while 1:
    if Timer.RunAfter(a1):
        print ('you will see this in every 3000ms')

    if Timer.RunAfter(a2):
        print ('you will see this in every 2000ms')

    if Timer.RunAfter(a3):
        print ('you will see this in every 1000ms')

    if Timer.RunAfter(a4):
        print ('you will see this in every 100ms')
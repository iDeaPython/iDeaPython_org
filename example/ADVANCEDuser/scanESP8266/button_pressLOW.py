'''
THIS PROGRAM FOR HACKING BUTTON ON scanESP8266
1. Run the program on esp8266
2. Press the button which you want to test.bat, you can hold it during "cooldown". FYI a button may control more than one GPIO
3. REPL will show your the result.
'''


import time
from machine import Pin
GPIOLIST=[0,2,4,5,12,13,14]

def countdown(i):
    for j in range(i):
        # print (j+1)
        time.sleep( 1 )

for i in GPIOLIST:
    globals()['GPIO'+ str(i)]=Pin(i,mode=Pin.IN,pull=Pin.PULL_UP)
a=0
print ('press the button on esp')
while 1:
    for i in GPIOLIST:
        if globals()['GPIO' + str(i)].value()==False:
            print( 'GPIO', i, 'has been PULLED DOWN')
            print( 'You press nothing, but you see this hint, the GPIO may be connected to a component such as relay' )
            a=1
    if a:
        print ('cooldown in 3s\n\n')
        countdown(3)
        a=0



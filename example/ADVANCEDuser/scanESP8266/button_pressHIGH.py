'''
THIS PROGRAM FOR HACKING BUTTON ON scanESP8266
1. Run the program on esp8266
2. Press the button which you want to test.bat, you can hold it for 1s, it may control more than one GPIO
3. REPL will show your the result.
'''


import time
from machine import Pin
GPIOLIST=[0,2,4,5,12,13,14,15]

def countdown(i):
    for j in range(i):
        # print (j+1)
        time.sleep( 1 )

for i in GPIOLIST:
    globals()['GPIO'+ str(i)]=Pin(i,mode=Pin.OUT)
a=0
print ('press the button on esp')
while 1:
    for i in GPIOLIST:
        if globals()['GPIO' + str(i)].value():
            print( 'GPIO', i, 'has been PULLED UP' )
            a=1
    if a:
        print ('cooldown in 3s')
        countdown(3)
        a=0



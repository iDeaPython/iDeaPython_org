'''
THIS PROGRAM FOR HACKING BUTTON ON scanESP8266
1. Run the program on esp8266
2. It will set GPIOs to high and low in every 3s
3. REPL will show your the result.
'''


import time
from machine import Pin
GPIOLIST=[0,2,4,5,12,13,14]

def countdown(i):
    for j in range(i):
        print (j+1)
        time.sleep( 1 )
for i in GPIOLIST:
    globals()['GPIO'+ str(i)]=Pin(i,mode=Pin.OUT)
for i in GPIOLIST:
    print ('GPIO',i, 'will be HIGH voltage for 3s')
    countdown(3)
    globals()['GPIO' + str(i)].value(1)
    print( 'GPIO', i, 'will be LOW voltage for 3s' )
    countdown( 3 )
    globals()['GPIO' + str(i)].value(0)


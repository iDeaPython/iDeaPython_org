# can't run FOXcollector.py in esp32(spiram), i don't know why? but ship.py runs well

from lib.COMMON.Collectors import collector
from lib.COMMON.management import lowSpeed as ast
from lib.COMMON.timer import Timer

astconn = collector( apparatus=ast ,initialSlot=0 )
print('Program Starting')
command='redColloctor!4_3:0-1'

print ('start high Speed\n')
from lib.COMMON.management import highSpeed as hs
hsconn = collector( apparatus=hs,H_CH=1,initialSlot=0 ,HSlen=3 )

print ('start low Speed\n')
from lib.COMMON.management import lowSpeed as ls
lsconn = collector( apparatus=ls,initialSlot=0 )

print ('start switch/power mode\n')
# from lib.COMMON.management import redColloctor as red  # problem, why can't use red??? because line 7('command='redColloctor!4_3:0-1'')???
# from lib.COMMON.management import blueColloctor as LINK
from lib.COMMON.management import redCollector as LINK
Collector = collector(apparatus=LINK)
# buttonActive
Collector.btn.addlink( [1], [2] )


while True:
    lsconn.send('000', LS_interval=3000)
    hsconn.send( '111' )
    if Timer.RunAfter('zzz1_5000'):
        astconn.askAssist(command)
    # Collector.askshipSwitch() # abandoned, just use Main()
    # press btn1 to control slot2, in redColloctor
    Collector.Main()


# use gui to produce codes automatically, these widgets can be installed on collector, and hints how many burdens already have
# As an esp8266, setup a highspeed is 90%, a lowspeed is 10%, a fire is 15%

# put some lowspeed class under the collector, they need id, but do i have to give them wifi name and passwd, i think yes


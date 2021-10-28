from lib.COMMON.Collectors import collector
from lib.COMMON.Trigger import trigger

from lib.COMMON.management import lowSpeed as ast
from lib.COMMON.timer import Timer
astconn = collector( apparatus=ast )
print('Program Starting')
command='5_3:0-1'

# high speed
from lib.COMMON.management import highSpeed as hs
hsconn = collector( apparatus=hs,H_CH=1 )

# low speed
from lib.COMMON.management import lowSpeed as ls
lsconn = collector( apparatus=ls )

# red collector
# weaponActive
from lib.COMMON.management import redColloctor as red
Collector = collector(apparatus=red, Slot=True)

#buttonActive

## Trigger
trigger(temp.equal(10), collector.laser.GetRawCMD('1:0_1'))
trigger(temp.equal(10), trigger(touch.done(), collector.laser.GetRawCMD('1:0_1')))

temp.equal(10).trigger(collector.laser.GetRawCMD('1:0_1')) # nope, this is stupid

##

while True:
    if Timer.RunAfter('zzz1_5000'):
        astconn.askAssist('redColloctor',command)
    hsconn.send('H234567890')
    if Timer.RunAfter('zzz2_1000'):
        lsconn.send('L234567890')
    Collector.askshipSwitch()
    # press btn1 to control slot2, in redColloctor
    Collector.btn.link([1], [2])


# use gui to produce codes automatically, these widgets can be installed on collector, and hints how many burdens already have
# As an esp8266, setup a highspeed is 90%, a lowspeed is 10%, a fire is 15%



# put some lowspeed class under the collector, they need id, but do i have to give them wifi name and passwd, i think yes



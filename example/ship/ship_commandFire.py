# POWER STRIP TEST ON scanESP8266, format is 'gpio1_0,gpio2_1,gpio3_0,gpio4_1'
from lib.COMMON.management import Data_AP as Main, redColloctor, blueColloctor, Fiona
from lib.COMMON.Ships import ship
from lib.COMMON.timer import Timer
conn = ship(WIFI=Main, Hint=1)
# command='1_2:1-1'
a=1
while True:
    conn.Main()
    if Timer.RunAfter('a1_6000'):
        if a:
            # conn.updateSwitch( apparatus=powerStrip_1, CMD=Main.CMD.slot3_ON_10s )
            conn.updateSwitch(apparatus=Fiona, CMD=Main.Fiona.ON)
            a=not a
        else:
            # conn.updateSwitch(apparatus=powerStrip_1, CMD=Main.CMD.slot3_ON)
            conn.updateSwitch(apparatus=Fiona, CMD=Main.Fiona.OFF)
            a = not a



'''
Users will use the color(red, green, blue) to control the weapon between colloctor and ship
example:
conn.updateSwitch(apparatus=powerStrip_1, CMD=Main.CMD.slot3_OFF)
into:
conn.updateSwitch(apparatus=powerStrip_1, CMD=Main.CMD.redMissile_OFF)

just change the name slot3_OFF into redMissile_OFF in management.py, it's ok.
'''
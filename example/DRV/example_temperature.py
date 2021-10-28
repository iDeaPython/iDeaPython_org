from lib.DRV.SENSOR.DS18X20 import TEMP
detect_interval=1000 # 1000ms
temp=TEMP()
while 1:
    if Timer.RunAfter('zzz1_',detect_interval):
        print ( temp.Is )
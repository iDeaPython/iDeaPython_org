from machine import Pin
from lib.COMMON.management import DS18X20
import time, ds18x20
import onewire

ow = onewire.OneWire(Pin(DS18X20.IO1))  # create a OneWire bus on GPIO12
ds = ds18x20.DS18X20(ow)

class TEMP():
    @property
    def Is(self, t=None):
        roms = ds.scan()
        ds.convert_temp()
        for rom in roms:
            if t==None:
                return (ds.read_temp(rom)+1.2)
            elif ds.read_temp(rom)+1.2>=t:
                return 1
            # print (ds.read_temp(rom)+2.2)

# dth11
# am2301

# This has been abandoned

from lib.COMMON.Collectors import collector
from lib.COMMON.management import Fiona as Main
Collector = collector( apparatus=Main ) # "switch=True" is default

# install a Button, use "1" in Collector.btnToGPIO to control "2" in Collector.slotToGPIO

# link=Collector.button(Collector.btnToGPIO,[1],Collector.slotToGPIO, [2])

while 1:


    Collector.askshipSwitch()


# new action, collector send L data to ship, it can change the status of link
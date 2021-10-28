
from lib.COMMON.Collectors import collector
from lib.COMMON.management import Fiona as Main
Collector = collector( apparatus=Main ) # "switch=True" is default

# install a Button, use "1" in Collector.btnToGPIO to control "2" in Collector.slotToGPIO
def remote():
    # Collector.remoteLink([1], [1], 'redCollector',locked=1) #  make "redColloctor" add a btnlink ([1], [1] ) tested
    Collector.remoteLink([1,2], [1,2], 'redCollector',locked=1) #  make "redColloctor" add a btn 1,2 to control slot 1,2  tested

while 1:
    Collector.Main()
    remote()
    # Collector.btn.link( [1], [2] )  # Btn1 controls Slot2 reference from management.py



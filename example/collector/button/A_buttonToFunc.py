# This has been abandoned
from lib.COMMON.Collectors import collector
from lib.COMMON.management import Fiona as Main
Collector = collector( apparatus=Main )

# install a Button, use "1" in Collector.btnToGPIO to control "2" in Collector.slotToGPIO
# Collector.btn.addlink([1], [1])
def test():
    print ('press btn [1] test')

while 1:
    Collector.Main()
    if Collector.btn.Pressed([1]):
        test()
     # Btn1 controls Slot1 reference from management.py



# new action, collector send L data to ship, it can change the status of link
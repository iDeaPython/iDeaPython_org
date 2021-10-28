# This has been abandoned
from lib.COMMON.Collectors import collector
from lib.COMMON.management import Fiona as Main
Collector = collector(apparatus=Main, Slot=True)

# install a Button, use "1" in Collector.btnToGPIO to control "2" in Collector.slotToGPIO

# link=Collector.button(Collector.btnToGPIO,[1],Collector.slotToGPIO, [2])

while 1:
    Collector.btn.link([1], [2]) # Btn1 controls Slot1 reference from management.py
    Collector.askshipSwitch()


# new action, collector send L data to ship, it can change the status of link
# This has been abandoned
from lib.COMMON.Collectors import collector
from lib.COMMON.management import Fiona as Main
Collector = collector( apparatus=Main )

# install a Button, use "1" in Collector.btnToGPIO to control "2" in Collector.slotToGPIO

# link=Collector.button(Collector.btnToGPIO,[1],Collector.slotToGPIO, [2])
# Collector.btn.addlink([1], [1], locked=1) # locked means the self-lock button tested
Collector.btn.addlink([1,2], [1,2], locked=1) # locked means the self-lock button tested
print('Program Starting')
while 1:
     # Btn1 controls Slot1 reference from management.py
    Collector.Main()

# new action, collector send L data to ship, it can change the status of link


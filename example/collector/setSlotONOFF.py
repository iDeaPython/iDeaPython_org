from lib.COMMON.Collectors import collector
from lib.COMMON.management import lowSpeed as Main
from lib.COMMON.timer import Timer

conn = collector(apparatus=Main)
print('Program Starting')


while True:
    # createTask(Assist(),1)

    conn.switch.setSlot(1,True)

    conn.Main()


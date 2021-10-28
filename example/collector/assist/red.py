from lib.COMMON.Collectors import collector
from lib.COMMON.management import redCollector as Main

conn = collector(apparatus=Main)
print('Program Starting')

while True:
    conn.Main()
    # createTask(Assist(),1)




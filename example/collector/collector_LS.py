from lib.COMMON.Collectors import collector
from lib.COMMON.management import lowSpeed as Main
conn = collector(apparatus=Main,Hint=1)
print('Program Starting')
a=100
while True:
    a+=1
    conn.send(str(a), LS_interval=3000) # can't send repeated data
    conn.Main()


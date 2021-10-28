from lib.COMMON.Collectors import collector
from lib.COMMON.management import highSpeed as Main
conn = collector(apparatus=Main, H_CH=1)
print('Program Starting')
while True:
    conn.send('1234567890',repeatable=1)



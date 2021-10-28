from lib.COMMON.Collectors import collector
from lib.COMMON.management import lowSpeed as Main
from lib.COMMON.timer import Timer
conn = collector(apparatus=Main)
print('Program Starting')
def Assist():
    # conn.askAssist('4_3*0-1@redCollector') # , make slot 3 and 4 turn on.
    # conn.askAssist('1*0-1@redCollector') # , make slot 1 turn on. tested.
    # conn.askAssist('1*4-3@redCollector') # , make slot 1 turn on, it lasts 4s, then turn off, after 4s turn on again, repeat this 3 times tested
    conn.askAssist('1_2*4-3@redCollector') # , make slot 1 and 2 turn on, it lasts 4s, then turn off, after 4s turn on again, repeat this 3 times tested
while True:
    conn.Main()
    # if conn.btn.Pressed([1]):
    Assist()


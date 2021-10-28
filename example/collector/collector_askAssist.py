from lib.COMMON.Collectors import collector
from lib.COMMON.management import lowSpeed as Main
from lib.COMMON.timer import Timer
conn = collector(apparatus=Main)
print('Program Starting')
def Assist():
    # conn.askAssist('redColloctor!4_3*0-1') #old way
    # conn.askAssist('4_3*0-1@redCollector') #new way
    conn.askAssist('0*5-5@redCollector')    #new way
    # conn.askAssist('0*0-1@redCollector')  #new way
    # conn.askAssist('0*0-0@redCollector')  #new way
while True:
    # createTask(Assist(),1)
    if Timer.RunAfter('testAssist', 1000):
        # conn.askAssist('Fiona',command)
        Assist()

    conn.Main()
# collector connect to ship to ask other collectors to have an assistance
# A collector ask collector 3 fire, then send a str 'assist_3:1-1' to ship

# conn.assist('5_3*1-1')


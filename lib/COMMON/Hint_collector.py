# collector

def out(t,p=''):
    pass

def OUT(t,p=''):
    if p==None:
        p='None'
    if t == 1:
        print('connect WIFI')
    elif t==2:
        print('HS MODE')
    elif t==3:
        print('Slot MODE')
    elif t ==4 :
        print('pure LS MODE')
    elif t ==5:
        print('receive id:', p)
    elif t ==6:
        print('WIFI has already CONNECTED')
    elif t ==7:
        print('trying connect to high speed port: ' + p)
    elif t ==8:
        print('\n\nH_clientSocket is 1\n\n')

    elif t ==9:

        print(' CH has been occupied ')
    elif t ==10:

        print(' can not receive the response from high speed port 8000 ')
    elif t ==21:
        print('Please Delete "!" from your name!')
    elif t ==12:
        print('Non-Responsed-Times in ask ship: ', p)

    elif t ==13:
        print('Be offline')
    elif t ==14:
        print('received reassignID')
    elif t ==15:
        print('\nRecv DATA: ', p, '\n')
    elif t ==16:
        print('recv: check')
    elif t ==17:

        print(' Highspeed data can not send.')
    elif t ==18:
        print('after', p, 'sec will be reboot')
    elif t ==19:
        print('low speed sent data: ', p[0] + p[1])
    elif t ==20:
        print('received string: reassign')


# elif t ==:
# elif t ==:
# elif t ==:
# elif t ==:
# elif t ==:
# elif t ==:

# ship

def out(t,p=''):
    pass

def OUT(t,p=''):
    if p==None:
        p='None'
    if t == 1:
        # print('%04d' % p[0], 'update switchDict: ', p[1]['%04d' % p[0]])
        print('id',p[0], ', name',p[1],' have been stored in switchDict: ')
    elif t==2:
        print('send generate ID: ', p)
    elif t==3:
        print('GOT SHAKE_DATA: ', p)
    elif t ==4 :
        print('recv from connLength: ', p)
    elif t ==5:
        print('CLOSE    connLength      AND     socketLength')
    elif t ==6:
        print('can not recv length H_ch')
    elif t ==7:
        print('NO request port 8000, done.')
    elif t ==8:
        print('bound port: ' + str(p[0][p[1]]))
    elif t ==9:
        print('CLOSE    connLength      AND     socketLength, start to receive high speed data ')
    elif t ==10:
        print('NO connections-request on port: ', p)
    # no t==11
    elif t ==12:
        print('send reassignID, and regular socket is closed')
    elif t ==13:
        print('received LS raw/shakedata data: ', p[0], p[1])
    elif t ==14:
        print('received assist fire data')
    elif t ==15:
        print('the name need to be altered is :', p)
    elif t ==16:
        print('ID ' + p[0] + ' can be updated: ', p[1])
    elif t ==17:
        print('ID ' + p + ' ask to update, but not in switch_dict so far')
    elif t ==18:
        print('\nsending updated data to client :', p[0] + p[1], '\n\n')
    elif t ==19:
        print('regular socket is closed')
    elif t ==20:
        print('high speed CHANNEL-' + p + ' has got lost: ')
    elif t ==21:
        print(p + ' closed')
    elif t ==22:
        print(p + ' closed')
    elif t ==23:
        print('Hdata_str: ' + p)
    elif t ==24:
        print('Sentry patrols online list: ', p)
    elif t ==25:
        print('collector offline, deleted ID:', p)
    elif t ==26:
        print('Sentry patrols may be offline: ', p)

# elif t ==:
# elif t ==:
# elif t ==:
# elif t ==:
# elif t ==:
# elif t ==:

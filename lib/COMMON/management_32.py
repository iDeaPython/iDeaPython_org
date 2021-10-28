# THIS MANAGEMENT.PY IS AN EXAMPLE
class Sword_AP():
    ssid = 'Sword_AP'
    passwd = '123456789'
    IPprefix = '192.168.4.'

    class IO():
        MC_IN = 22
        RELAY_OUT = 27

    class CMD():
        Lhand = '1:1-1'
        Rhand1 = '1_2:1-1'
        Rhand2 = '1_2:4-1'  # S1,S2, begin from ON at once, next running is opposite of beginning, after interval of round = 4s, start by round-cycle, 1 round in all
        target = '1:10-1'


class SWORD_Lhand():  # touch electrical light, it was foot before
    ssid = Sword_AP.ssid
    passwd = Sword_AP.passwd
    IPprefix = Sword_AP.IPprefix
    ID = 17
    SlotTotal = 1
    Slot1 = 4  # d2, GPIO4
    # cmd = '1:1-1' # S1, begin from ON immediately, next running is opposite of beginning, after interval of round= 0.5s,, start by round-cycle, 1 round in all.


class SWORD_Rhand():  # hold the swordWithMC
    ssid = Sword_AP.ssid
    passwd = Sword_AP.passwd
    IPprefix = Sword_AP.IPprefix
    ID = 18
    SlotTotal = 2
    Slot1 = 14  # d5, GPIO14
    Slot2 = 12  # d6, GPIO12
    # cmd_2 = '1_2:4-1' # S1,S2, begin from ON at once, next running is opposite of beginning, after interval of round = 4s, start by round-cycle, 1 round in all
    # cmd_2 = '1:8-5,2:2-9'  # S1,S2, begin from ON at once, next running is opposite of beginning, after interval of round = 4s, start by round-cycle, 1 round in all


class SWORD_target():
    ssid = Sword_AP.ssid
    passwd = Sword_AP.passwd
    IPprefix = Sword_AP.IPprefix
    ID = 19
    SlotTotal = 1
    Slot1 = 0  # d3, GPIO0
    # cmd = '1:10-1' # S1, begin from ON immediately, next running is opposite of beginning, after interval of round= 10s,, start by round-cycle, 1 round in all.


class CAR():
    ssid = 'CAR_AP'
    passwd = '123456789'
    IPprefix = '192.168.4.'
    ID = 13
    D_sensor = False


class Data_AP():
    ssid = 'Data_AP'
    passwd = '123456789'
    IPprefix = '192.168.4.'

    SlotTotal = 10
    Slot1 = 4
    Slot2 = 5
    Slot3 = 13
    Slot4 = 14
    Slot5 = 15
    Slot6 = 16
    Slot7 = 17
    Slot8 = 18
    Slot9 = 19
    Slot10 = 21

    BtnTotal = 7
    Btn1 = 22
    Btn2 = 23
    Btn3 = 25
    Btn4 = 26
    Btn5 = 27
    Btn6 = 32
    Btn7 = 33


    class CMD():  # this part can be defined in a name # it's not able to be generated by SC_GUI
        No1 = '3:1-1'
        No2 = '2:3-1'
        slot3_ON_10s = '3:10-1'
        slot3_OFF = '3:0-0'
        slot3_ON = '3:0-1'
    class Fiona(): # it's not able to be generated by SC_GUI
        ON = '1_2:0-1'
        OFF = '1_2:0-0'

class highSpeed():  # for test
    ssid = Data_AP.ssid
    passwd = Data_AP.passwd
    IPprefix = Data_AP.IPprefix

    SlotTotal = 10
    Slot1 = 4
    Slot2 = 5
    Slot3 = 13
    Slot4 = 14
    Slot5 = 15
    Slot6 = 16
    Slot7 = 17
    Slot8 = 18
    Slot9 = 19
    Slot10 = 21

    BtnTotal = 7
    Btn1 = 22
    Btn2 = 23
    Btn3 = 25
    Btn4 = 26
    Btn5 = 27
    Btn6 = 32
    Btn7 = 33


class lowSpeed():  # for test
    ssid = Data_AP.ssid
    passwd = Data_AP.passwd
    IPprefix = Data_AP.IPprefix

    SlotTotal = 10
    Slot1 = 4
    Slot2 = 5
    Slot3 = 13
    Slot4 = 14
    Slot5 = 15
    Slot6 = 16
    Slot7 = 17
    Slot8 = 18
    Slot9 = 19
    Slot10 = 21

    BtnTotal = 7
    Btn1 = 22
    Btn2 = 23
    Btn3 = 25
    Btn4 = 26
    Btn5 = 27
    Btn6 = 32
    Btn7 = 33

class redColloctor():
    ssid = Data_AP.ssid
    passwd = Data_AP.passwd
    IPprefix = Data_AP.IPprefix
    # prefix of "Slot", "Button" is irrevocable.
    SlotTotal = 10
    Slot1 = 4
    Slot2 = 5
    Slot3 = 13
    Slot4 = 14
    Slot5 = 15
    Slot6 = 16
    Slot7 = 17
    Slot8 = 18
    Slot9 = 19
    Slot10 = 21

    BtnTotal = 7
    Btn1 = 22
    Btn2 = 23
    Btn3 = 25
    Btn4 = 26
    Btn5 = 27
    Btn6 = 32
    Btn7 = 33

class blueColloctor():
    ssid = Data_AP.ssid
    passwd = Data_AP.passwd
    IPprefix = Data_AP.IPprefix
    # prefix of "Slot", "Button" is irrevocable.
    SlotTotal = 10
    Slot1 = 4
    Slot2 = 5
    Slot3 = 13
    Slot4 = 14
    Slot5 = 15
    Slot6 = 16
    Slot7 = 17
    Slot8 = 18
    Slot9 = 19
    Slot10 = 21

    BtnTotal = 7
    Btn1 = 22
    Btn2 = 23
    Btn3 = 25
    Btn4 = 26
    Btn5 = 27
    Btn6 = 32
    Btn7 = 33


class Fiona():
    ssid = Data_AP.ssid
    passwd = Data_AP.passwd
    IPprefix = Data_AP.IPprefix
    # prefix of "Slot", "Button" is irrevocable.
    SlotTotal = 10
    Slot1 = 4
    Slot2 = 5
    Slot3 = 13
    Slot4 = 14
    Slot5 = 15
    Slot6 = 16
    Slot7 = 17
    Slot8 = 18
    Slot9 = 19
    Slot10 = 21

    BtnTotal = 7
    Btn1 = 22
    Btn2 = 23
    Btn3 = 25
    Btn4 = 26
    Btn5 = 27
    Btn6 = 32
    Btn7 = 33

class Richard():
    ssid = Data_AP.ssid
    passwd = Data_AP.passwd
    IPprefix = Data_AP.IPprefix



# for example
class DS18X20():
    IO1 = 4  # d2

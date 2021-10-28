import socket
from lib.COMMON.timer import Timer
from machine import reset

def return_conn( port):
    count = 0
    while count < 5:
        try:
            conn1 = socket.socket()
            conn1.connect(('192.168.4.1', port))
            return conn1
        except:
            count += 1
        Timer.delayMS(750)  #
    print('can not connect to server port: ' + str(port))
    return 0

class TCP():
    def __init__(self):
        self.receivable = 0
        # self.n = self.__dict__
        self.conn=0
        self.count=0
    def _recv_data(self, conn, length):
        try:
            recv = conn.recv( length ).decode()
        except:
            recv = '_'
        return recv

    def send(self,data,port,mode= 'waiting',returnConn=0,autoReset=0):
        if self.receivable == 0:  # "isHalfduplex_recv" only for SWITCH MODE
            conn = return_conn(int(port))
            if conn != 0:
                self.count=0
                conn.send(data.encode())
                self.conn = conn
            else:
                self.count+=1
                if self.count>30:
                    reset()
                # return 1
                return '_'
        if self.conn != 0:
            if mode == 'waiting':
                self.conn.settimeout(6)
            elif mode == 'halfduplex' and self.receivable == 0:
                self.conn.settimeout(0)
                self.receivable = 1
                return 'receiving'
            elif mode == 'halfduplex':
                self.receivable = 0
            recv = self._recv_data(self.conn, 26)
            if returnConn != 1:
                self.conn.close()
                self.conn=0
                return recv
            return self.conn, recv
        else:
            if returnConn == 1:
                return 0,'_'
            else:
                return '_'

class UDP():
    def send(self, port, data):
        count = 0
        while 1:
            try:
                conn = socket.socket()
                conn.connect( ('192.168.4.1', port) )
                # self._send_data( conn, data )
                conn.send( data.encode() )
                conn.close()
                break
            except:
                count += 1
                Timer.delayMS(800)
                if count > 4:
                    # uos.dupterm(uart, 1)  # for moment when test
                    print('UDP can not send.')
                    return 0
                    # machinereset()  # for moment when officially start to use







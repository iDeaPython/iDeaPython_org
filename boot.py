from lib.COMMON.timer import Timer
# from lib.COMMON.CreateTask import createTask
from machine import reset
Timer.init()
import network
nic = network.WLAN(network.STA_IF)
if nic.active():
    nic.active(False)
ap = network.WLAN(network.AP_IF)  # create access-point interface
if ap.active():
    ap.active(False)  # activate the interface

del (nic,ap)
import gc
gc.collect()

#today
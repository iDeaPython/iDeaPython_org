# EXAMPLE broker.py:
from lib.COMMON.Ships import ship
from lib.COMMON.management import Data_AP as Main
conn = ship(Host=Main, Slot=1, Hint=1)
while True:
    conn.Main()


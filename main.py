import time
from pymouse import PyMouse


def sleeptime(hour, min, sec):
    return hour*3600 + min*60 + sec


second = sleeptime(0, 3, 0)
m = PyMouse()
a = m.position()
while 1 == 1:
    m.click(86.2265625, 288.7578125)
    time.sleep(second)

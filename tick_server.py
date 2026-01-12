#
# Simple Tick Data Server
#
import zmq
import time
import random
import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://0.0.0.0:5555')

AAPL = 100.

while True:
    AAPL += random.gauss(0, 1) / 2
    # msg = f'AAPL {AAPL:.2f}'
    obj = {'TIME': str(datetime.datetime.now()),
           'SYMBOL': 'AAPL', 'PRICE': round(AAPL, 2)}
    # print(msg)
    print(obj)
    # socket.send_string(msg)
    socket.send_pyobj(obj)
    time.sleep(random.random() * 2)

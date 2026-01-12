#
# Simple Tick Data Server
# (2 simulated stock prices)
#
import zmq
import time
import random
import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://0.0.0.0:5555')

AAPL = 100.
MSFT = 100.

while True:
    if random.random() < 0.5:
        AAPL += random.gauss(0, 1) / 2
        obj = {'TIME': str(datetime.datetime.now()),
           'SYMBOL': 'AAPL', 'PRICE': round(AAPL, 2)}
    else:
        MSFT += random.gauss(0, 1) / 2
        obj = {'TIME': str(datetime.datetime.now()),
           'SYMBOL': 'MSFT', 'PRICE': round(MSFT, 2)}
    print(obj)
    socket.send_pyobj(obj)
    time.sleep(random.random() / 2)

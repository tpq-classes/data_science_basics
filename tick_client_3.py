#
# Simple Tick Data Client
# (for persisting collected data)
#
import zmq
import pandas as pd

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://0.0.0.0:5555')
socket.setsockopt_string(zmq.SUBSCRIBE, '')

ticks = pd.DataFrame()

while True:
    obj = socket.recv_pyobj()
    df = pd.DataFrame(obj, index=[0])
    ticks = pd.concat((ticks, df), ignore_index=True)
    print(obj)
    if len(ticks) % 7 == 0:
        ticks.set_index('TIME').to_hdf('ticks.h5', key='data',
                     mode='a', format='table', append=True)
        print('TICKS WRITING')
        ticks = pd.DataFrame()

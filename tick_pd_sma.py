#
# Tick Data Signals with pandas
#
import zmq
import pandas as pd
import sqlite3 as sq3

class TickPDSignal:
    def __init__(self, url):
        self.url = url
        self.ticks = pd.DataFrame()
        self.connect_socket()
    def connect_socket(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(self.url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, '')
    def generate_signals(self, lags):
        while True:
            msg = self.socket.recv_pyobj()
            df = pd.DataFrame({'symbol': msg['SYMBOL'], 'price': msg['PRICE']},
                              index=[pd.Timestamp(msg['TIME'])])
            self.ticks = pd.concat((self.ticks, df))
            no = len(self.ticks)
            if no % 20 == 0:
                data = self.ticks[self.ticks['symbol'] == 'AAPL']
                sma = data.iloc[-lags:]['price'].mean()
                price = data.iloc[-1]['price']
                signal = 'long' if sma > price else 'short'
                templ = f'{no} | SMA={round(sma, 2)} | '
                templ += f'PRICE={price} | SIGNAL={signal}'
                print(templ)
                #print(no, round(sma, 2), price, signal)

if __name__ == '__main__':
    pd_signal = TickPDSignal('tcp://0.0.0.0:5555')
    pd_signal.generate_signals(10)


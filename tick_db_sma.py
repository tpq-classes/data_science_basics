#
# Tick Data SQLite3 Signals
#
import sqlite3 as sq3

class TickDBSignals:
    def __init__(self, file):
        self.file = file
        self.connect_database()
    def connect_database(self):
        self.connection = sq3.connect(self.file)
        self.cursor = self.connection.cursor()
    def generate_signals(self, lags):
        no_last = 0
        while True:
            no = self.cursor.execute('SELECT COUNT(*) FROM ticks').fetchall()[0][0]
            if no % 20 == 0 and no > no_last:
                no_last = no
                data = self.cursor.execute('''SELECT * FROM ticks WHERE symbol ==
                "AAPL" ORDER BY id DESC''').fetchmany(lags)
                prices = [d[3] for d in data]
                sma = sum(prices) / len(prices)
                price = prices[0]
                signal = 'long' if sma > prices[0] else 'short'
                templ = f'{no} | SMA={round(sma, 2)} | '
                templ += f'PRICE={price} | SIGNAL={signal}'
                print(templ)

while __name__ == '__main__':
    db_signals = TickDBSignals('../tick_data.sq3')
    db_signals.generate_signals(10)

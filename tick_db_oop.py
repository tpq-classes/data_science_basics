#
# OOP Tick Database
#
import zmq
import sqlite3 as sq3

class TickDatabase:
    def __init__(self, url, file):
        self.url = url
        self.file = file
        self.connect_socket()
        self.connect_database()
    def connect_socket(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(self.url)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, '')
    def connect_database(self):
        self.connection = sq3.connect(self.file)
        self.cursor = self.connection.cursor()
        self.cursor.execute('PRAGMA journal_mode=WAL')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ticks
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT, symbol TEXT, price REAL)''')
    def retrieve_and_write(self):
        while True:
            msg = self.socket.recv_pyobj()
            print(msg)
            self.cursor.execute('''INSERT INTO ticks
                    (date, symbol, price)
                    VALUES (?, ?, ?)''',
                    (msg['TIME'], msg['SYMBOL'], msg['PRICE']))
            self.connection.commit()


#
# Simple Tick Database with SQLite3
#
import zmq
import sqlite3 as sq3

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

con = sq3.connect('../ticks.db')
cursor = con.cursor()
# cursor.execute('PRAGMA journal_mode=WAL')
cursor.execute('''CREATE TABLE IF NOT EXISTS ticks
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT, symbol TEXT, price REAL)''')

while True:
    msg = socket.recv_pyobj()
    print(msg)
    cursor.execute('''INSERT INTO ticks
                (date, symbol, price)
                VALUES (?, ?, ?)''',
        (msg['TIME'], msg['SYMBOL'], msg['PRICE']))
    con.commit()

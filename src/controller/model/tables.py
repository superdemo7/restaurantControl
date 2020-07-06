from tinydb import TinyDB, Query

class Table():
    def __init__(self):
        db = TinyDB('db.json')
        self.table = db.table('tables')
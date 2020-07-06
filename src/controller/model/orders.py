from tinydb import TinyDB, Query
class Order():
    def __init__(self):
        db = TinyDB('db.json')
        self.table = db.table('orders')
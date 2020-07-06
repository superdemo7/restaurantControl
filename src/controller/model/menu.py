from tinydb import TinyDB,Query

class Menu():
    def __init__(self):
        db = TinyDB('db.json')
        self.table = db.table('menu')
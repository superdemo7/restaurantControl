from tinydb import TinyDB, Query

class Table():
    def __init__(self):
        db = TinyDB('db.json')
        self.table = db.table('tables')
    def all(self):
        return self.table.all()
    def addTable(self, name):
        return self.table.insert({"name":name})
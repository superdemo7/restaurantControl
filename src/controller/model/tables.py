from tinydb import TinyDB, Query

class Table():
    def __init__(self):
        db = TinyDB('db.json')
        self.table = db.table('tables')
    def all(self):
        all_tables = []
        tables = self.table.all()
        for table in tables:
            newTable = table
            newTable["id"] = table.doc_id
            all_tables.append(newTable)
        return all_tables
    def addTable(self, name):
        return self.table.insert({"name":name})
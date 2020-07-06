from tinydb import TinyDB, Query

class User():
    def __init__(self):
        db = TinyDB('db.json')
        self.table = db.table('users')
        total_users = self.all()
        if not total_users:
            self.register('admin','admin123','admin')
        self.user = None
    def all(self):
        all_users = []
        users = self.table.all()
        for user in users:
            new_user = user
            new_user['id'] = user.doc_id
            all_users.append(new_user)
        return all_users
    def register(self,name, password, user_type):
        return self.table.insert({
            'name':name,
            'password': password,
            'type':user_type
        })
    def getById(self, id):
        user = self.table.get(doc_id=id)
        return user
    def getUser(self):
        return self.user
    def setUser(self, id):
        user = self.table.get(doc_id=id)
        newUser = user
        newUser["id"] = user.doc_id
        self.user = newUser
    def clearUser(self):
        self.user = None
        return True

        
    
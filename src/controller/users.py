import eel
import sys
from .model import User
user = User()
@eel.expose
def users_getAll():
    return user.all()
@eel.expose
def users_login(id,password):
    response = {
        "success" : False,
        "msg":""
    }
    _user = user.getById(id)
    if _user:
        if _user['password'] == password:
            user.setUser(id)
            response["type"] = _user["type"]
            response["success"] = True
        else:
            response["msg"] = "Contraseña incorrecta"
    else:
        response["msg"] = "Este ID no existe"
    return response
@eel.expose
def users_getUser():
    return user.getUser()
@eel.expose
def users_logout():
    return user.clearUser()

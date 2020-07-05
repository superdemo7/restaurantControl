import eel
@eel.expose
def login(username, password):
    response = { "success":False,"msg":"" }
    if username == "":
        response["msg"] = "Usuario no puede estar vacio"
    elif password == "":
        response["msg"] = "Contraseña no puede estar vacia"
    else:
        response["success"] = True
    return response
eel.init('src/view/dist')
eel.start('index.html')
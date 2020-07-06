import eel
from .model import Table
table = Table()
@eel.expose
def tables_getAll():
    return table.all()
@eel.expose
def tables_addTable(newTable):
    response = {
        "success":False,
        "msg":""
    }
    if not newTable:
        response["msg"] = "Nombre de tabla no puede estar vacio"
    else:
        table.addTable(newTable)
        response["success"] = True
    return response
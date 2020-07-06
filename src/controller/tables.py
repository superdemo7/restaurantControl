import eel
from .model import Table
table = Table()
@eel.expose
def tables_getAll():
    return
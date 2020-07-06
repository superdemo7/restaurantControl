import eel
from .model import Table
@eel.expose
def tables_getAll():
    return
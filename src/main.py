import eel

#Controladores
from controller import *

eel.init('src/view/dist')
eel.start('index.html',cmdline_args=['--start-fullscreen'])
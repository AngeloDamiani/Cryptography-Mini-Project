import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.chat.view.gui as gui

import src.chat.model.Client as client

name = str(sys.argv[1])
portrcv = int(sys.argv[2])
porttx = int(sys.argv[3])
g = gui.TkinterGui()
c = client.Client(name, porttx, portrcv, g)
c.start()
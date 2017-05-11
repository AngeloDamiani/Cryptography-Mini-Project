import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from client.view import TkinterGui
from client.model import Client

name = str(sys.argv[1])
portrcv = int(sys.argv[2])
porttx = int(sys.argv[3])
g = TkinterGui()
c = Client(name, porttx, portrcv, g)
c.start()
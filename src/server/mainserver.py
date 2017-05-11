import os.path
import sys
from model.Server import Server

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

s = Server()
s.start()



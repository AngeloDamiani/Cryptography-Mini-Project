import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from keyserver.model import RSAKeyServer

s = RSAKeyServer()
s.start()



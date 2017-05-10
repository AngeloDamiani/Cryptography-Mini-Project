import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import src.chat.model.Server as server

s = server()
s.start()



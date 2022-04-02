import time
import sys
from color import *

def bar():
    toolbar_width = 40
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in range(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write(cyan("="))
        sys.stdout.flush()
    sys.stdout.write("]\n")

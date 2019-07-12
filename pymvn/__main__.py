import sys

from pymvn.init import *
from pymvn.integrate import *


if __name__ == "__main__":
    if len(sys.argv) == 1:
        package()
    elif sys.argv[1] == "init":
        init()
        sys.exit(0)


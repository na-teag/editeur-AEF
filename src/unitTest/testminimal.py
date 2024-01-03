from data.structure import createAutomate
from editing.minimal import toMinimal
from editing.minimal import isMinimal

GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'

a = createAutomate()


print(f"input automate is minimal: {a.isMinimal()}")
b = toMinimal(a)
if b.isMinimal():
    print(f"{GREEN}Test successful{ENDC}")
else:
    print(f"{RED}Test failed{ENDC}")
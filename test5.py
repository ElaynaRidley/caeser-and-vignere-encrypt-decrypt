from EBox import *

ebox = EBox()
ebox.reset("encrypt", 0)
ebox.set_password("CATZ");
x = ebox.encrypt("dig trenches at dawn")
print(x)
print(ebox.get_status())

x = ebox.encrypt("the cat yawned at dawn and then slept the rest of the day")
print(x)
print(ebox.get_status())

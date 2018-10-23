from EBox import *

ebox = EBox()
ebox.reset("decrypt", 0)
ebox.set_password("CATZ");
x = ebox.decrypt("FIZITE61JEBZVDTLP")
print(x)

#  expected output:
#  DIG TRENCHES AT DAWN
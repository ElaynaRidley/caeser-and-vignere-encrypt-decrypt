from EBox import *

ebox = EBox()
ebox.reset("encrypt", 1)
ebox.set_password("CATZ");
expect =  "FIZIUF72LGD1YGWOTXBMYN0E1N39WLCU"
print("Expect: " + expect)
x = ebox.encrypt("dig trenches at dawn to trick the enemy")
print("Actual: " + x)
if (expect == x): print("***PASSED***")
print("")

print("  (the faulty algorithm) ")
expect = "FIZITE61JEBZVDTLPT7ITIV9VHX3PE5N"
print("Expect: " + expect)
x = ebox.encrypt("dig trenches at dawn to trick the enemy")
print("Actual: " + x)
if (expect == x): print("***PASSED***")

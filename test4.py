from EBox import *

ebox = EBox()
ebox.reset("decrypt", 1)
ebox.set_password("CATZ");
expect = "DIGTRENCHESATDAWNTOTRICKTHEENEMY"
print("Expect: " + expect)
x = ebox.decrypt("FIZIUF72LGD1YGWOTXBMYN0E1N39WLCU")
print("Actual: " + x)
if (expect == x): print("***PASSED***")
print("")

print("  (the faulty algorithm) ")
print("Expect: " + "DIGTRENCHESATDAWNTOTRICKTHEENEMY")
x = ebox.decrypt("FIZITE61JEBZVDTLPT7ITIV9VHX3PE5N")
print("Actual: " + x)
if (expect == x): print("***PASSED***")

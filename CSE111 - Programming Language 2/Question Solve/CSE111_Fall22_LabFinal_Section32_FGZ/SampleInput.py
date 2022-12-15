from LabFinal_s32 import *

g1 = Grandfather("Azmir Khan", 45)
g1.display()
Grandfather.display_title()
Grandfather.display_wealth()

f1 = Father("Mehedi Hasan", 30, 50000)
f1.display()
print(Father._title)
Father.display_wealth()

m1 = Mother("Mehjabin", 25)
m1.display()

s1 = Son("Kabir Hasan", 5, 50000, "Programming")
s1.display()

d1 = Daughter("Sadia", 3, "Dancing")
d1.display()
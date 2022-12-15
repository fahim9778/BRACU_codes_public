# Click CodeCheck to check your code
##HIDE
from SampleInput import *

g1.display()
print("Expected: My name is Azmir Khan and I am 45 years old. My title is Khan and I have 1 Crore in my bank account.")
Grandfather.display_title()
print("Expected: My title is Khan")
Grandfather.display_wealth()
print("Expected: My wealth is 1 Crore")

f1 = Father("Mehedi Hasan", 30, 50000)
f1.display()
print("Expected: My name is Mehedi Hasan and I am 30 years old. My title is Hasan and I income 50000 per month."\
    "\nI have Black hair and Brown eyes.")
print(Father._title)
print("Expected: Hasan")
Father.display_wealth()
print("Expected: You are not a Khan. You can't access my wealth.")

m1 = Mother("Mehjabin", 25)
m1.display()
print("Expected: My name is Mehjabin and I am 25 years old. I have Red hair and Blue eyes.")

s1 = Son("Kabir Hasan", 5, 50000, "Programming")
s1.display()
print("Expected: My name is Kabir Hasan and I am 5 years old. My title is Hasan and I income 50000 per month.")
print("Expected: I have Black hair and Brown eyes.")
print("Expected: I have hobby of Programming.")

d1 = Daughter("Sadia", 3, "Dancing")
d1.display()
print("Expected: My name is Sadia and I am 3 years old. I have Red hair and Blue eyes.")
print("Expected: I like Dancing.")

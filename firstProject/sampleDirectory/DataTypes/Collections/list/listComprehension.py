# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 15th Dec, 2016
# Title  : List Comprehension
# Description : Comprehension done on list.
# Tested On   : python 3.5.0

x = [p * p for p in range(10)]
print(x)

x = range(10)
y = [p * p for p in x]
print(y)

x = [p for p in range(11) if p % 2 == 0]
print(x)

y = []
for p in range(11):
    if p % 2 == 0:
        y.append(p)
print(y)

z = [q**q for q in range(10)]
print(z)

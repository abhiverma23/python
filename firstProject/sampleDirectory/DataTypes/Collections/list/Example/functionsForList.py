# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 13th Dec, 2016
# Title  : List Examples
# Description : Functions can be applied on list.
# Tested On   : python 3.5.0

x = [10, 70, 30, 20, 40, 60]
print(max(x))
print(min(x))
print(sorted(x))
print(x)
rev = reversed(x)
for i in rev:
    print(i)
for j in reversed(sorted(x)):
    print(j)

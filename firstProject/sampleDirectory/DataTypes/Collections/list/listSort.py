# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 15th Dec, 2016
# Title  : List Operations
# Description : Sorting and appending.
# Tested On   : python 3.5.0

x = [30, 20, 40, 60, 10]
print(x)
print(id(x))
x.append(60)
print(x.sort())
print(x)
print(id(x))
x.remove(30)
print(x)
y = ['hello', True, 12.12]
x.extend(y)
print(x)

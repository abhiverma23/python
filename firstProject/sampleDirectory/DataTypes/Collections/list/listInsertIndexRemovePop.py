# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 15th Dec, 2016
# Title  : List Operations
# Description : Insert, index, pop and remove.
# Tested On   : python 3.5.0

x = [10, 'hyd', True, 123.123]
print(x)
x.insert(2,30)
print(x)
print(x.index(True))
x.pop()
x.pop(2)
print(x)
x.remove('hyd')
print(x)

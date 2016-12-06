# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 5th Dec, 2016
# Title  : String Concatenation
# Description : Concatenating two string into other variable.
# Tested On   : python 3.5.0

x = 'Hello'
print(x)
print(id(x))

y = ' World'
print(y)
print(id(y))

z = x+y
print(z)
print(id(z))
print(id(x))
print(id(y))

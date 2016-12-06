# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 5th Dec, 2016
# Title  : Input different data type values value
# Description : Taking input from keyboard and converting to integer.
# Tested On   : python 3.5.0

x = input("Enter int value")
print(type(x))
i = int(x)
print(type(i))

y = input("Enter float value")
print(type(y))
j = float(y)
print(type(j))

z = input("Enter complex value")
print(type(z))
k = complex(z)
print(type(k))

a = input("Enter boolean value")
print(type(a))
b = bool(a)
print(type(b))

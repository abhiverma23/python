# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 6th Dec, 2016
# Title  : Checking Mutability
# Description : LIST : overwriting in same object
# Tested On   : python 3.5.0

x = [10,20,30,40]
print(x)
print(id(x))

x[1] = 50
print(x)
print(id(x))

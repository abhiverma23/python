# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 11th Dec, 2016
# Title  : List
# Description : List and describing it's values using for while loop.
# Tested On   : python 3.5.0

x = [10, 20, 30, 40]
i = 0
while i < len(x):
    print(x[i], type(x[i]), id(x))
    i += 1

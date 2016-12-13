# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 11th Dec, 2016
# Title  : List
# Description : List inside list.
# Tested On   : python 3.5.0

x = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(x)
print(type(x))
for p in x:
    print(p, type(p))
    for q in p:
        print(q, type(q))

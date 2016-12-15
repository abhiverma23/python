# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 13th Dec, 2016
# Title  : List Examples
# Description : Matrix addition.
# Tested On   : python 3.5.0

a = [[10,20,30],
     [40,50,60],
     [70,80,90]]
b = [[10,20,30],
     [40,50,60],
     [70,80,90]]

c = [[],[],[]]

for i in range(3):
    for j in range(3):
        c[i].append(a[i][j]+b[i][j])

print(c)

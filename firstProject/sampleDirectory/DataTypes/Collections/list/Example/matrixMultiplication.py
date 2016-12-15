# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 13th Dec, 2016
# Title  : List Examples
# Description : Matrix multiplication.
# Tested On   : python 3.5.0

a = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]]
b = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]]

c = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            p = str(i)+" "+str(k)
            q = str(k)+" "+str(j)
            c[i][j] += a[i][k] * b[k][j]

print(c)

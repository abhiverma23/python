# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 13th Dec, 2016
# Title  : List Examples
# Description : Adding elements in list.
# Tested On   : python 3.5.0

x = [10, 20, 30, 40]

sum = 0
for p in x:
    sum += p
print(sum)

i = 0
sum1 = 0
while i < len(x):
    sum1 += x[i]
    i += 1
print(sum1)

# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 13th Dec, 2016
# Title  : List Examples
# Description : Printing list data in ascending order of names.
# Tested On   : python 3.5.0

x = [[1001, 'scott', 2000],
     [1002, 'ravana', 20000],
     [1003, 'sita', 1000]]
for p in x:
    print(p)

names = []
for a in x:
    names.append(a[1])

print(names)
print(sorted(names))

final = []

for a in sorted(names):
    for z in x:
        if a == z[1]:
            final.append(z)
print(final)

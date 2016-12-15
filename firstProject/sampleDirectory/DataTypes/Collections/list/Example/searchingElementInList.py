# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 13th Dec, 2016
# Title  : List Examples
# Description : Searching elements in list.
# Tested On   : python 3.5.0

x = [10, 20, 30, 40]

e = int(input("Enter search element"))
if e in x:
    print("Element found")
else:
    print("Element not found")

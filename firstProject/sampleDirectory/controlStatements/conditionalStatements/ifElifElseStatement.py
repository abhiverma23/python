# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 9th Dec, 2016
# Title  : Conditional Statement
# Description : if...[[elif...][else...]] statement.
# Tested On   : python 3.5.0

print("Begin")

x = int(input("Enter a positive value"))

if x < 10:
    print("Given number is 1 digit number")
elif x < 100:
    print("Given number is 2 digit number")
elif x < 1000:
    print("Given number is 3 digit number")
else:
    print("Given number is >=4 digit number")

print("End")

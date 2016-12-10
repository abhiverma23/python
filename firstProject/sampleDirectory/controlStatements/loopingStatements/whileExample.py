# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 10th Dec, 2016
# Title  : While Example 001
# Description : Asking username and password with in while loop so we can ask again if either is wrong.
# Tested On   : python 3.5.0

while True:
    name = input("enter Username")
    if name != 'sharma':
        continue
    password = input("Hello, Sharma. What is the password?")
    if password == 'anshu':
        break
print('Access Granted.')

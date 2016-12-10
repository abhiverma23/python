# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 9th Dec, 2016
# Title  : Conditional Statement
# Description : Example of : if...[[elif...][else...]] statement.
# Tested On   : python 3.5.0

name = input ("Enter name")
age = int(input('Enter age'))
if name == 'Alice':
    print("Hi Alice.")
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 10th Dec, 2016
# Title  : Looping Statement
# Description : while statement with continue statement.
# Tested On   : python 3.5.0

print("begin")
i = 0
while i <= 10:
        i += 1
        if i == 5:
            continue
        print("hi", i)
print("end")

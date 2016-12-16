# Author : Abhishek Verma
# E-Mail : abhishekverma3210@gmail.com
# Date   : 15th Dec, 2016
# Title  : List Prime
# Description : Generating prime and non prime number using list comprehension.
# Tested On   : python 3.5.0

noprimes = [j for i in range(2,8) for j in range(i*2, 50, i)]
primes = [x for x in range(2,50) if x not in noprimes]
print(primes)

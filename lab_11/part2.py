
'''
Purpose: Lets user to print fibonacci to a file

Pre-conditions: user enters number of files to write

Post-conditions: Gives out the fibonacci numbers of the file

BY: Edris Shahem   THURSDAY LAB
''' 
import random
# opening and writing to our fibonacci.txt file
f = open("fibonacci.txt","w")
f.write('0'+"\n") 
f.write('1'+"\n")
# creating our first function and passing in number
def fibonacci(num):
    f = open ("fibonacci.txt","w")
    n1, n2 = 0, 1

    for i in range (2, num+1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        f.write(str(n3) + "\n")

num = int(input("How many Fibonacci numbers would you like to get: "))
fibonacci(num)
f1=open("fibonacci.txt", 'r') 
data=f1.read().split() 
value_a=0

for i in data:
    print(str(value_a)+str(i))
    value_a+=1
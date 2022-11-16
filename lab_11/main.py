'''
Purpose: Lets user to print to a file
    and find prime numbers

Pre-conditions: user enters number of files to write

Post-conditions: Gives out the prime numbers of the file

BY: Edris Shahem   THURSDAY LAB
''' 

import random
# Creating a function to check for prime
def check_prime(num):
    for i in range (2, num):
        if num & i == 0:
            return 1
    return 0
# Creating a function to write in prime.txt
def write_value(n):
    outfile = open ("prime.txt", "w")
    for i in range (n):
        outfile.write(str(random.randint (1,100))+"\n")

    outfile.close ( )
# Asking user input
num = int(input( "\nHow many number are needed to write the file: "))
print("******************************\n")
# Calling our function
write_value(num)

f = open ("prime.txt", "r")
data = f.read ( )
data = data.split()

string_1 = ""

for i in data:
    string_1 += i + " "

print (string_1, "\n" )

string_2 = ""
count = 0

for i in data:
    if check_prime(int(i)) == 0:
        count += 1 
        string_2 += i + " "
# Printing the numbers found
print (string_2)
print (count, "prime number found in this file")
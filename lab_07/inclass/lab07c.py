"""
Program: CS 1301 Lab 06
Author: Edris Shahem

Description: This program will read a positive integer and
i_num press it as the sum of powers of 2.

"""
def main():
     # Read user's input and store it as an integer in a variable called i_num.
    i_num = int(input("Enter a number: "))
    calculate(i_num)

# creating another function to calculate
def calculate(i_num):
    list = []
     # while i_num is larger than zero:
    while (i_num>0):
        list.append(int(i_num % 2))
        i_num = int(i_num/2)
    for i in range(len(list)-1, 0, -1):
        if(list[i] == 1):
            print("2**",i, sep="", end="")
            if i>1:
                print(" + ", end="")
main()
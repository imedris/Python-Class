import random 
import string
import os
# function to generate passwords
def generate_password():
    # Clearing the console
    os.system('cls')
    
    # Asking for user's input
    print("\nPassword Generator Program")
    print("______________________________")

    length = int(input("How many characters for your password? "))
    password_count = int(input("How many passwords would you like: "))
    secure_input = input("Toggle extra secure password?(y/n): ")
    # Adding extra security if user chooses yes
    if secure_input == "yes" or secure_input == "y":
        chars = secure_password()
    else:
        chars = string.ascii_letters + string.digits
    
    count = 0
    # Using nested for loop with user's input
    for x in range(0,password_count):
        password = ""
        for x in range(0,length):
            # using the random library to make random choice
            password_char = random.choice(chars)
            password += password_char
        count += 1  
        # calling our suffix function to add suffix
        count_str = str(count_suffix(count))
        print("Your "+ count_str + " password: " + password)

def secure_password():
    # Using the string library to generate 
    #     characters and digits
    chars = string.ascii_letters + string.digits + string.punctuation
    return chars

# Creating a function to attach suffix
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def count_suffix(num):
    # using dictionary to store st nd rd
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')
    # this function returns the number with its suffix
    return str(num) + suffix

# calling main function
generate_password()

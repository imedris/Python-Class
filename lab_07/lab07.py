'''
Purpose: offer the user a choice of food items, calculate total bill

Pre-conditions: user enters 5 or 6 y's or n's depending on desired items
(string)

Post-conditions: prompts for choices, total bill before (float) and after
tip, (float) and parting message.
''' 
 

def main():
    # Name of Restaurant 
    print ('Welcome to Diary King.')
    # give user instructions of expected inputs 
    print ('Please answer each question with y or n.')
    # initialize total bill to zero 
    totalPrice=0.0 
     # ask first choice 
    user_input=input('Do you want a grilled cheese sandwich?')
    if user_input =='y' or user_input=='Y':
        #add price to total bill 
        totalPrice+=7
    user_input=input ("Do you want a serving of nachos? ") 
    if user_input =='y' or user_input=='y':
        totalPrice+=5
    user_input=input ("Do you want a chicken sandwich? ") 
    if user_input=='y' or user_input=='Y':
        totalPrice+=8
    user_input=input ("Do you want a Hamburger? ") 
    # if hamburger is selected only then we prompt the user if he she wants cheese 
    if user_input=='y' or user_input=='Y':
        totalPrice+=8
        user_input=input ("Do you want cheese on that? ") 
        if user_input=='y' or user_input=='Y':
            totalPrice+=10
    user_input=input ( "Do you want a hot dog? ") 
    if user_input=='y' or user_input=='Y':
        totalPrice+=6
    calculate_tip(totalPrice)

def calculate_tip(totalPrice):
    with_tip=(totalPrice*0.2)+totalPrice 
    # output blank line
    print("\n")
    #Calculating the total price with tip 
    print ("The total for your food is $"+"{:.2f}".format(totalPrice))
    print ("The total with 20 % tip is $"+"{:.2f}".format(with_tip)) 
    # rounding our answer till 2 decimal places 
    print ("Thank you for your business.")

main()
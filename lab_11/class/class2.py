# creating feet to steps function
def feet_to_steps(user_feet):
    # calculating feet
    return user_feet // 2.5

# running the function
if __name__ == '__main__':
    user_feet = float(input("Input: "))
    print('{:.0f}'.format(feet_to_steps(user_feet)))
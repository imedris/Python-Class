
# Activity 1
laps = 7.6
def lapToMile(laps):
    return laps * 0.25

if __name__ == '__main__':
    print(f'{lapToMile(laps):.2f}')


# Activity 2
mpg = 20
dollar = 3.1599
def cost_of_driving(mpg, dollar, miles):
    return miles / mpg * dollar

if __name__ == '__main__':
    print(f'\n{cost_of_driving(mpg, dollar, 10):.2f}')
    print(f'{cost_of_driving(mpg, dollar, 50):.2f}')
    print(f'{cost_of_driving(mpg, dollar, 400):.2f}')
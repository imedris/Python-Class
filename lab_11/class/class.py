# Creating a function to get value from user
def input_save():
    miles_per_gallon = float(input("Enter 1st: "))
    dollars_per_gallon = float(input("Enter 2nd: "))
# using for loop using miles list
    miles = [10, 50, 400]
    for i in miles:
        print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, i):.2f}')
# calculating driving cost by following formua
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return dollars_per_gallon / miles_per_gallon * miles_driven

def print_answer():
    cost = driving_cost(20.0,3.1599, 50.0)
    print(f'{cost:.2f}')


if __name__ == '__main__':
    input_save()

def exact_change (user_total):
    num_quarters = user_total // 25
    user_total %= 25
    num_dimes = user_total // 10
    user_total %= 10
    num_nickels = user_total // 5
    user_total %= 5
    num_pennies = user_total
    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == '__main__':
    input_val = int (input ( ))
    num_pennies, num_nickels, num_dimes,num_quarters = exact_change(input_val)
    
    if (input_val == 0):
        print ( 'No change')
    else:
        if num_pennies > 1:
            print ('%d pennies' % num_pennies)

        elif num_pennies == 1:
            print ('%d penny' % num_pennies)

        if num_nickels > 1:
            print ('%d nickels' % num_nickels)

        elif num_nickels == 1:
            print ('%d nickel' % num_nickels)

        if num_dimes > 1:
            print ('%d dimes' % num_dimes)

        elif num_dimes == 1:
            print ('%d dime' % num_dimes)

        if num_quarters > 1:
            print ('%d quarters' % num_quarters)

        elif num_quarters == 1:
            print ('%d quarter' % num_quarters)
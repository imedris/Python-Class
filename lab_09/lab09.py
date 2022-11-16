'''
Purpose: Lets the user find Hex to RGB

Pre-conditions: user enters a Hex color

Post-conditions: Spits out the RGB color of the given hex

BY: Edris Shahem   THURSDAY LAB
''' 

# Finding Red color
def get_red(example):
    return int(example[0:2], 16)
# Green color
def get_green(example):
    return int(example[2:4], 16)
# Blue color
def get_blue(example):
    return int(example[4:6], 16)

def id_protanopia(example):
    # storing value of function in red var
    red = get_red(example)
    if red < 64:
        return "Protanopia: True"
    else:
        return "Protanopia: False"

def id_deuteranopia(example):
    green = get_green(example)
    if green < 64:
        return "Deuteranopia: True"
    else:
        return "Deuteranopia: False"

def id_tritanopia(example):
    red = get_red(example)
    green = get_green(example)
    blue = get_blue(example)
    if red > 230 and blue > 0 and green > 220:
        return "Tritanopia: False"
    else:
        return "Tritanopia: True"

def run_tests():
    # Running tests and calling functions
    hex = '4d6285'
    print(get_red(hex))
    print(get_green(hex))
    print(get_blue(hex))
    print(id_protanopia(hex))
    print(id_deuteranopia(hex))
    print(id_tritanopia(hex))

run_tests()
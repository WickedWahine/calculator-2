"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

#Start loop to receive calculation request
while True:
    input_string = input("Calculate > ")
    tokens = input_string.split(' ')
    operator = tokens[0]
    
    #Allow user to quit calculator app
    if 'q' in tokens:
        print("You will exit")
        break
    else:
        if len(tokens) < 2:
            print("I need at least 1 operator and 1 number")
            continue
        elif len(tokens) == 2:
            num1 = float(tokens[1])
        elif len(tokens) == 3:
            num1 = float(tokens[1])
            num2 = float(tokens[2])
        else:
            print("Include no more than 2 numbers")
            continue

    if operator == "+":
        print(add(num1, num2))

    elif operator == "-":
        print(subtract(num1, num2))

    elif operator == "*":
        print(multiply(num1, num2))

    elif operator == "/":
        print(divide(num1, num2))

    elif operator == "pow":
        print(power(num1, num2))

    elif operator == "mod":
        print(mod(num1, num2))   

    elif operator == "cube":
        print(cube(num1))

    elif operator == "square":
        print(square(num1))

    else:
        print("I need one operator followed by numbers")
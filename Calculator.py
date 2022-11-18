print("Enjoy this personal calculator")

question = input("Would you like to add, subtract, multiply, or divide? ")

if question == "add":
    add = int(input("Please enter the first number you wish to add: "))
    add_two = int(input("Please enter the second number: "))
    total = add + add_two
    print(total)

elif question == "subtract":
    subtract = int(input("Please enter the first number you wish to subtract: "))
    subtract_two = int(input("please enter the second number: "))
    total_two = subtract - subtract_two
    print(total_two)

elif question == "multiply":
    multiply = int(input("Please enter the first number you wish to multiply: "))
    multiply_two = int(input("Please enter the second number you wish to multiply: "))
    total_three = multiply * multiply_two
    print(total_three)

elif question == "divide":
    divide = int(input("Please enter the first number you wish to divide: "))
    divide_two = int(input("Please enter the second number you wish to divide: "))
    total_four = divide / divide_two
    print(total_four)

else:
    print("Input not accepted: please pick pick either add, subtract, multiply, or divide")



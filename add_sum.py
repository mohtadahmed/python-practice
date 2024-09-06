# =======================================================================
# Problem Statement
# Write a function that takes two numbers as input and returns their sum.
# =======================================================================

# Function for adding two numbers
def add_number(a,b):
    firstNumber = float(a)
    secondNumber = float(b)

    result = firstNumber + secondNumber

    return result


# Function for check the validity of the input value
def get_valid_input(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print('Please Enter a valid number')



a = get_valid_input("Enter First Number: ")

b = get_valid_input("Enter Second Number: ")



result = add_number(a,b)

print('Your first number is:', a)
print('Your second number is:', b)
print('The sum of two number is:', result)
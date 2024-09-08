# =======================================================================
# Problem Statement
# Write a function that checks if a given number is even or odd.
# =======================================================================

# Function for the detection of Odd or Even number
def detect_odd_even(number):
    if (number % 2) == 0:
        return 'Even'
    else:
        return 'Odd'

# Function for error handling
def get_only_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print('Enter a valid integer')

number = get_only_number('Enter an integer number: ')

result = detect_odd_even(number)

# Print the result
print(f'The number {number} is {result}.')
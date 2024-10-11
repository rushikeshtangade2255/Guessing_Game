from random import randint

# Get the range from user input1
try:
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
except ValueError:
    print("Invalid input, please enter integers.")
    exit()

# Ensure lower_bound is less than upper_bound
if lower_bound >= upper_bound:
    print("The lower bound should be less than the upper bound.")
    exit()

# Generate a random number in the range
random_number = randint(lower_bound, upper_bound)

# Main guessing loop
while True:
    try:
        number = int(input(f'Please choose a number between {lower_bound} and {upper_bound}: '))
        if lower_bound <= number <= upper_bound:
            if number == random_number:
                print("You're a genius!")
                break
            else:
                print("Try again!")
        else:
            print(f"Please enter a number within the range {lower_bound} to {upper_bound}.")
    except ValueError:
        print("Please enter a valid number.")

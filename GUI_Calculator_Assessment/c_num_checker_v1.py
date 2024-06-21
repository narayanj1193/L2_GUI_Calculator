# Simple number checker to check for integers.
def num_checker(question):
    while True:

        try:
            response_integer = int(input(question))  # checks user input to make sure it is integer
            return response_integer

        except ValueError:  # catches value error that would be prompted incase if user inputs non-integer
            print("Please respond with a sensible integer. Please try again.")
            continue


amount_rounds = num_checker("How many rounds? ")
rounds_completed = 0
while amount_rounds > rounds_completed:
    rounds_completed += 1
    user_equation = num_checker("What is your equation? ")

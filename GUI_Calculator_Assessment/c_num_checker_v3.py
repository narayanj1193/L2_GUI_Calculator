import fractions
from c_basic_int_checker import int_checker


# Function that checks if an input is valid. If int_only is false it works well for equations, as it allows all sorts
# of inputs including floats and strings. Took this from a previous project
def num_check(question, int_only=True):
    error = "Please enter a valid number or 'xxx' to exit."

    while True:
        response = input(question)

        if response == "xxx":
            return "end_game"

        elif response == "":
            if int_only:
                # If an empty string is entered and only integers are allowed, return the empty string
                return response
            else:
                print(error)
                continue

        elif response != "":
            if not int_only:
                response = str(response)

                # If non-integer values are allowed, check for special cases and evaluate the response
                if response.lower() == 'x' or ('x' in response.lower() and '+' in response or '-' in response):
                    # If the response contains 'x' with '+' or '-', return the response
                    return response

                if '^' in response and '2' in response:
                    # If the response contains '^' and '2', return the response
                    return response

                try:
                    number = eval(response)
                    if isinstance(number, float) or isinstance(number, int) or isinstance(number, fractions.Fraction):
                        # If the evaluated response is a float, integer, or fraction, return the number
                        return number
                    else:
                        print(error)
                        continue

                # error handling
                except (NameError, ZeroDivisionError, SyntaxError, TypeError, SyntaxWarning):
                    print(error)
                    continue

        else:
            # If int_only is True, use the int_checker function for validation
            validated_response = int_checker(response, error)

            if validated_response == "end_game":
                return "end_game"

            else:
                return validated_response

amount_rounds = num_check("How many questions will you be asking? ")
rounds_completed = 0

while amount_rounds > rounds_completed:
    rounds_completed += 1
    user_equation = num_check("What is your equation? ", False)
    print(user_equation)
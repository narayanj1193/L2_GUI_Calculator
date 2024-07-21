def int_checker(response, error):
    if response == "xxx":
        return "end_game"

    # if int_only is true, use a basic integer checker
    else:
        try:
            # Check that the response is an integer
            response = int(response)

            # if the amount is too low or too high
            if response < 1 or response > 50:
                print("Please enter an integer that is more than 1 and less than 50.")

        except ValueError:
            print(error)

    return response

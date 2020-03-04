# Class resources used for loops
# Understanding Babylonian formula: http://mathshistory.st-andrews.ac.uk/HistTopics/Babylonian_mathematics.html
# Absolute value in Python: https://www.geeksforgeeks.org/abs-in-python/

print("Welcome to the square-root calculator")
format = str(input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: " ))
if format == "single":
    user_input = float(input("Please enter a positive number: "))
    guess = user_input/2
    threshold = 0.0001
    second_guess = guess**2-user_input

# Take a guess (x/2), then compute second guess (x^2 - (x/2)) where if parameter holds true
    # take average of previous guess and x/guess. Iteratively use formula until closest value is determined.

    if user_input >= 0:
        while True:
            second_guess = guess**2-user_input
            if abs(second_guess)<threshold:
                break
            guess = (guess+user_input/guess)/2
        print("The square root of", user_input, "is", round(guess, 3))
    elif user_input < 0:
        print("Error: Please enter a positive number")

elif format == "range":
    min = float(input("Please enter a positive integer value to start your range: "))
    if min >= 0:
        max = float(input("Please enter a positive integer value to end your range: "))
        guess = min/2
        threshold = 0.0001

        if min >= max:
            print("Error: Please try again. ")

        elif max >= 0:
            while True:
                count = min
                second_guess = guess**2-min
                if abs(second_guess)<threshold:
                    break
                guess = (guess+min/guess)/2
            print("Number", '\t', "Square-root", '\n', min, '\t', round(guess, 3))
            while True:
                count = count + 1
                second_guess = guess**2-count
                if abs(second_guess)<threshold:
                    break
                guess = (guess+count/guess)/2
                print('\n', count, '\t', round(guess, 3))
                if count == max:
                    break
        elif max < 0:
            print("Error: Please enter a positive number")

    else:
        print("Error: Please enter a positive number")
else:
    print("Error: Please enter 'single' or 'range' ")



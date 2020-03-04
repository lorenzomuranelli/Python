# Help from additional sources:
# https://stackoverflow.com/questions/34952669/how-to-get-python-compound-interest-calculator-to-give-the-correct-answer
# https://www.programming-techniques.com/2019/03/python-program-to-calculate-compound-interest.html
# https://www.includehelp.com/python/program-for-compound-interest.aspx
# https://docs.python.org/3/library/functions.html#round
# https://www.w3resource.com/python-exercises/python-basic-exercise-113.php

# Python program to calculate compound interest. Prompts user to enter numbers and will display results.
# Uses the equation P′=P(1+r/n)nt
# User must enter a numeric value, otherwise they will have to restart.

print("Welcome to the Compound Interest Calculator!")
while True:
    try:
        p = float(input("Please enter the initial amount of your investment: "))
        r = float(input("Please enter the interest rate (decimal): "))
        c = int(input("Please enter the number of compoundings per year (e.g., 12 for monthly compounding, 4 for quarterly, 1 for annual): "))
        t = int(input("Please enter the number of years of the investment: "))
        break
    except ValueError:
        print("You must enter a numeric value. Please try again.")
        print()

# Compound interest equation
ci = p * (((1 + (r/(100.0 * c))) ** (c*t)))

# Results
print("Original investment of", "$", round(p, 2))
print("The amount of interest earned is", "$", round(ci - p, 2))
print("The total value of the account after", t, "years is", "$", round(ci, 2))

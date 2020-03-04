# Program that asks for the age and gender of an individual, and based on that information,
# prints the Recommended Daily Allowance for Calcium
# Pregnant or lactating question only for females in the age range of 14 to 50.
# Sources:
# https://stackoverflow.com/questions/37826322/get-a-specific-input-in-python
# http://pythonfiddle.com/question-5-for-computer-science/

print("Welcome to the Recommended Daily Allowance for Calcium calculator!")
gender = input(("Please enter the gender of the individual (m=male, f=female): "))

if gender == "m":
    age = float(input("Please enter the age of the individual in years (e.g., .5 for 6 months, .58 for 7 months, etc.): "))
    result = str()
    print(result)
    if 0 <= age <= .5:
        result = "200 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif .58 <= age < 1:
        result = "260 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 1 <= age <= 3:
        result = "700 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 4 <= age <= 8:
        result = "1000 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 9 <= age <= 13:
        result = "1300 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 14 <= age <= 18:
        result = "1300 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 19 <= age <= 50:
        result = "1000 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 51 <= age <= 70:
        result = "1000 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    elif 71 <= age:
        result = "1200 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old male is", result, ".")
    else:
        print("Error: Please try again.")

if gender == "f":
    age = float(input("Please enter the age of the individual in years (e.g., .5 for 6 months, .58 for 7 months, etc.): "))
    result = str()
    print(result)
    if 0 <= age <= .5:
        result = "200 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif .58 <= age < 1:
        result = "260 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 1 <= age <= 3:
        result = "700 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 4 <= age <= 8:
        result = "1000 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 9 <= age <= 13:
        result = "1300 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 14 <= age <= 18:
        Q = str(input("Are you pregnant or lactating? (Enter 'yes' or 'no') "))
        if Q == "yes":
            print("The recommended daily allowance of calcium for a", age, "year old female who is pregnant or lactating is 1300 milligrams.")
        elif Q == "no":
            result = "1300 milligrams"
            print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 19 <= age <= 50:
        question = str(input("Are you pregnant or lactating? (Enter 'yes' or 'no') "))
        if question == "yes":
            print("The recommended daily allowance of calcium for a", age, "year old female who is pregnant or lactating is 1000 milligrams.")
        elif question == "no":
            result = "1000 milligrams"
            print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 51 <= age <= 70:
        result = "1200 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    elif 71 <= age:
        result = "1200 milligrams"
        print("The recommended daily allowance of calcium for a", age, "year old female is", result, ".")
    else:
        print("Error: Please try again.")




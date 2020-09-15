file=input("Please enter the name of the input data file: ")
try:
    fhand = open(file)
    for lines in fhand:
        lines = lines.rstrip()
        #print(line)
except:
    print('File cannot be opened. Please re-enter the file-name.')
    exit()

# Output file
outcome=input("Please enter the name of the output data file: ")
# Curve
curveValue=input("Would you like to curve the grades?(Y/N) ")
curve=0
if curveValue=="Y":
    curve=int(input("Please enter the score that should map to a '100%' grade: "))

# GRAD
def grade(grade_level, score):
    if(grade_level == "GRAD"):
        if(score>=95):
            return "H\n"
        elif(score>=80 and score<95):
            return "P\n"
        elif(score>=70 and score<80):
            return "L\n"
        else:
            return "F\n"

# UNDERGRAD
    elif(grade_level == "UNDERGRAD"):
        if(score>=90):
            return "A\n"
        elif(score>=80 and score<90):
            return "B\n"
        elif(score>=70 and score<80):
             return "C\n"
        elif(score>=60 and score<70):
            return "D\n"
        else:
            return "F\n"

# Output + appending new
def output(file, outcome, curveValue):
    person = list()
    file = open(file, "r")
    line = file.readline()
    i = 0
    lst = list()
    while(line):
        if(line[-1] == '\n'):
            lst.append(line[:-1])
        else:
            lst.append(line)
        i = i + 1
        if(i==3):
        #if(i=3):
            if(lst[0] != "GRAD" and lst[0] != "UNDERGRAD"):
                print("Unknown student category detected (",lst[0],").")
                print("Error occurred while determining letter grade. Aborting.")
                return
        # isnumeric to make sure value is a number. If it's not, error message.
            if(lst[2].isnumeric()==False):
                print("Invalid score.")
                print("Error evaluating letter grade.")
                return
        # appended line on output.txt
            person.append(lst)
            lst = []
            i = 0
        line = file.readline()
    final = open(outcome, "w")

# Curving grade
    for i in range(len(person)):
        final.write(person[i][1]+ "\n")
        result = int(person[i][2])
        if(curveValue > 0):
            result = result + int(result * curveValue / 100)
        final.write(grade(person[i][0], result))
    final.close()
    print("All data was successfully processed and saved to the requested output file.")
output(file, outcome, curve)

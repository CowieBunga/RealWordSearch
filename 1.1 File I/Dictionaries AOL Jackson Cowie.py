'''
def extremeTuple(args):
    if len(args) > 0:  # if args has a length greater than 0, then the function will return max and min values
        maximum = max(args)
        minimum = min(args)
        return maximum, minimum
    else:  # otherwise, it reutrns zero, which contains the string below
        zero = "Your tuple contained no arguments"
        return zero
list1 = []
while True:  # loop allows the user to input multiple values
    nums = input("Input a number: ")
    if len(nums) > 0:  # it only appends to the list if a value was inputted (otherwise, the tuple's length will > 0
        list1.append(nums)
    again = input("Would you like to input another value? (no to exit) ")
    if again == 'no':
        break  # breaks the loop once user is done inputting numbers.
args = tuple(list1)  # turns the list to a tuple
results = extremeTuple(args)  # results is either max and min or zero depending on the length
print(results)  # prints the correct returned value
'''

import csv
data = {}
info = []
names = ('Jackson', 'Alex', 'Becky', 'Jeremy', 'Chris', 'Owen')

with open('database', 'r') as database:
    read = csv.reader(database)
    rows = [row for row in read]

for i in range(len(rows)):
        data[names[i]] = rows[i]

while True:
    name = input("Please input the first name of the student you would like to search: ").title()
    if name in names:
        fname = input("FIRST NAME? (y for yes) ")
        if fname == 'y':
            F = data[name][0]
        else:
            F = ''
        lname = input("LAST NAME? (y for yes) ")
        if lname == 'y':
            L = data[name][1]
        else:
            L = ''
        grade = input("GRADE? (y for yes) ")
        if grade == 'y':
            G = data[name][2]
        else:
            G = ''
        house = input("HOUSE? (y for yes) ")
        if house == 'y':
            H = data[name][3]
        else:
            H = ''
        advisor = input("ADVISOR? (y for yes) ")
        if advisor == 'y':
            A = data[name][4]
        else:
            A = ''
        print("FNAME: ", F)
        print("LNAME: ", L)
        print("GRADE: ", G)
        print("HOUSE: ", H)
        print("ADVISOR: ", A)
    else:
        print("That name was not in the database. Try again")

'''
def one_hop(flights, city1, city2):
    x = 0
    for item in flights[city1]:
        if item != city2:
            if city2 in flights[item]:
                x += 1
    if x >= 1:
        return True
    else:
        return False

flights = {'Montreal': ['Toronto', 'Tampa Bay'], 'Toronto': ['Montreal', 'Tampa Bay'],
               'Tampa Bay': ['Atlanta', 'Toronto'], 'Atlanta': ['Tampa Bay']}
city1 = input("Input first city: ").title()
city2 = input("Input second city: ").title()
print(one_hop(flights, city1, city2))
'''

'''
def choose_guess(guesses):
    if len(guesses) < 3:
        compguess = 2
    else:
        guesses = tuple(guesses)
        #print(guesses)
        combinations = {(1,1,1): 1, (1,1,2): 1, (1,2,2): 2, (2,2,2): 2, (2,1,1): 1, (2,2,1): 2, (2,1,2): 2, (1,2,1): 1}
        compguess = combinations[guesses]
    return compguess


userpoints = 0
comppoints = 0
guesses = []
# scores for user and comp ^
while comppoints < 30 and userpoints < 30:  # loop runs until someone reaches 30 points.
    x = 0
    guess = input("Input a number between 1 and 2 ")
    if guess == '1' or guess == '2':  # had to make it so the guesses were strings for defensive coding
        guesses.append(int(guess))
        if len(guesses) > 3:
            del guesses[0]
        if choose_guess(guesses) == int(guess):
            print("Computer got the point")
            comppoints += 1  # adds point for the comp
        else:
            print("User got the point")
            userpoints += 1  # adds point for the user
        print("User score:", userpoints)
        print("Computer Score:", comppoints)
        # prints out the score after each round

if userpoints > comppoints:  # outputs certain message depending on who got the higher score
    print("You Won! Congrats!")
else:
    print("You lost! The computer bested you.")

        #this loop above goes through the guesses and checks if they are 2's, and if so, adds it to a variable. to 
        calculate experimental probability (y) the number of times '2' shows up in the list of guesses is divided
        by the total number of guesses. If 2 shows up the majority of the time, then the computer will guess 2.
        otherwise, it will guess 1 
'''





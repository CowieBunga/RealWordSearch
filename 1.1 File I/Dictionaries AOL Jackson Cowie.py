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



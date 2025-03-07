#### ask user for an integer
### initiate the counter before the loop
### if a user types end, stop the loop
### if the user provides an intiger it does a factorial
### else increase the counter and redo the loop
# ## if the user does not provide integer
# ## prompt the user to try again


tries = 0 # this is my counter for the while true loop to calculate the number of bad ties 
allTries = 0
while True:
    allTries += 1

    userInput = input("Enter a number or type in end to exit: ")

    if userInput.lower() == "end":
        print(f"All total tries: {allTries-1}")
        print(f"Number of bad tries: {tries}")
        break # exit the loop

    if userInput.isdigit():
        number = abs(int(userInput))
        factorial = 1
        temp = number

        while temp>1:
            factorial *= temp
            temp -=1
        
        print(f"The fatorial of {number} is {factorial}")

    else:
        tries+=1
        print("You did not enter a number, please try again")
        print(f"Number of bad tries: {tries}")
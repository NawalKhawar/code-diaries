# Day 2: Number Guessing Game (With Hint System)

# ------ LIBRARIES ------
import random
import math


# ------------------ FUNCTIONS ------------------

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
# ----------------

def isPrime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True
    
# ----------------    
    
def generateRandomNumber():
    return random.randrange(1,1001) # between 1 and 1000 inclusive

# ----------------    

def checkDigitCount(n):
    return len(str(n))

# ----------------

def extractDigits(n):
    return [int(digit) for digit in str(n)]  # convert n to a string then extract digits

# ----------------    


def correctAnswerPrompt(tries, hintsRemaining):
    print("\n-------------------------------------------------------")
    print("☆* YAY! *☆")
    print("You guessed correctly, well done! :D")
    print("The answer is indeed", answer,".")
    print("You made a total of", tries, "tries, and used", 4 - hintsRemaining, "out of 4 hints!")
    print("-------------------------------------------------------\n")

# ----------------    

def startMessage():
    print("Hey there hooman bean. Let's play a game! (*^▽^*)\n")
    print("(∩^o^⊃━☆* I'm thinking of a number between 1 and 1000 (inclusive). Can you guess what it is? *☆.\n")

# ----------------    

def hintSystem(answer, hintsRemaining):
    if hintsRemaining == 4: # first hint - reveal count of digits
        digitCount = checkDigitCount(answer)
        print("[Hint 1/4] The number I'm looking for has", digitCount, "digits!")
    
    elif hintsRemaining == 3: # second hint - reveal if digit is even/odd, and prime/composite
        
        if isEven(answer):
            print("[Hint 2/4] The number I'm looking for is EVEN!")
            
        elif not isEven(answer) and isPrime(answer):
            print("[Hint 2/4] The number I'm looking for is ODD and PRIME!")
            
        else:
            print("[Hint 2/4] The number I'm looking for is ODD and COMPOSITE!")
        
    elif hintsRemaining == 2: # third hint - reveal a random digit in the number
        digits = extractDigits(answer) # array of extracted digits
        pos = random.randrange(1, checkDigitCount(answer) + 1) # randomly select a position in the number
        print("[Hint 3/4] The number I'm looking for has", digits[pos -1],"at position", pos, "(from the left)!")
        
    elif hintsRemaining == 1: # fourth hint - narrow the guessing range
        print("[Hint 4/4] The number I'm looking for is in the range", answer - 10,"to", answer + 15)
        
    else:
        print("\nWomp womp - you've used up all your hints! :(")
        
    print("\n")
    


# --------------- MAIN PROGRAM STARTS HERE ---------------

answer = generateRandomNumber()
userGuess = 0 # user's guess (initially 0)
tries = 0 # number of guesses made by the user
guessed = False 
hintStatus = 'N' # indicates whether or not user asked for a hint
hintsRemaining = 4 # total 4 hints

# game starts!
startMessage()

while not guessed:

    # present option of hint
    hintStatus = input("Would you like a hint? [Y/N] ")
    
    if hintStatus == 'Y' or hintStatus == 'y':
        hintSystem(answer, hintsRemaining)
        
        if hintsRemaining != 0: # only decrement remaining hint count if it's not already 0
            hintsRemaining -= 1
            
        hintStatus = 'N' # reset status
    
    
    # prompt user to make a guess
    userGuess = int(input("Take a guess: "))
    tries += 1
    
    if userGuess == answer: # user guessed correctly
        guessed = True
        
    else: #user guessed incorrectly
        if userGuess < answer:
            print("Nope! The number I'm looking for is GREATER than your guess!\n")
        else:
            print("Not quite...the number I'm looking for is LESS THAN than your guess!\n")
            
    continue

# user has correctly guessed the number
correctAnswerPrompt(tries, hintsRemaining)        
        


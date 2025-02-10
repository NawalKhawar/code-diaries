# Day 1: Simple Calculator

# Concepts Implemented:
#    - Functions
#    - Loops ('while')
#    - Conditional statements ('if-else')

#Thoughts: Python is so much simpler compared to C++ :')

# --------------------------------------
# CALCULATOR FUNCTIONS:
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2


# ---------------------------------------
# PRINT FUNCTIONS
def printMenu():
    print("************ MENU ************")
    print("KEYCODE          FUNCTION")
    print("  0                Exit")
    print("  1              Addition")
    print("  2             Subtraction")
    print("  3            Multiplication")
    print("  4               Division")
    print("******************************")
 
 
def printExitMessage():
    print("\nThat's it for now! See you next time! :)\n\n")



# -------------------------------------
# MAIN:
exited = False
A = -1
B = -1

print("Welcome to my calculator! :D \n\n")

while not exited:
    
    printMenu()
    
    #simulating a do-while loop for user input
    while True:
        userInput = int(input("Please enter the function you would like to perform: "))
        
        if userInput <= 4 and userInput >= 0: #input is in valid range
            break
        
        print("\nERROR: NUMBER OUT OF RANGE!\n")
    
    #user input completed
    
    if userInput == 0: #exit
        exited = True
        continue
    
    elif userInput == 1: #addition
        print("\n-------- ADDITION --------")
        print("FORMAT: A + B")
        A = int(input("Please enter A: "))
        B = int(input("Please enter B: "))
        print(" -> ", A, "+", B, "=", add(A, B))
        print("\n--------------------------\n\n")
        
        
    elif userInput == 2: #subtraction
        print("\n-------- SUBTRACTION --------")
        print("FORMAT: A - B")
        A = int(input("Please enter A: "))
        B = int(input("Please enter B: "))
        print(" -> ", A, "-", B, "=", subtract(A, B),"\n\n")
        print("\n-----------------------------\n\n")
        
        
    elif userInput == 3: #multiplication
        print("\n-------- MULTIPLICATION --------")
        print("FORMAT: A * B")
        A = int(input("Please enter A: "))
        B = int(input("Please enter B: "))
        print(" -> ", A, "+", B, "=", multiply(A, B))
        print("\n--------------------------------\n\n")
        
        
    elif userInput == 4: #division
        print("\n-------- DIVISION --------")
        print("FORMAT: A / B")
        A = int(input("Please enter A: "))
        B = int(input("Please enter B: "))
        print(" -> ", A, "/", B, "=", divide(A, B))
        print("\n--------------------------\n\n")

    
#calculator exited
printExitMessage()





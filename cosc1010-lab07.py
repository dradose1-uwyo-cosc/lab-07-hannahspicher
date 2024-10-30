# Hannah Spicher
# UWYO COSC 1010
# 10/29/24
# Lab 07
# Lab Section: 11
# Sources, people worked with, help given to: Textbook, Online Stack flow textbook, W3 schools textbook examples
# I used .lstrip to remove the negative sign in part one even though it wasn't mentioned until part 2 because the
# negative sign was causing the loop to return "please enter a numerical value" instead of "Please enter a positive 
# "number."
# Also in pt 3 I left the operand and operators defined inside of the while loop because it is re valued each time, but I 
# wasn't sure if it would work with it outside of the while loop and if that would have been cleaner. 


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered
while True:
    upperbound = input("Enter upper bound here:")
    if not upperbound.lstrip('-').isdigit():
        print("Please enter a numerical value.")
    else:
        upperbound=int(upperbound)
        if upperbound <=0:
            print("Please enter a positive number.")
        else:
            break  
factorial = 1
while upperbound > 1:
    factorial *= upperbound
    upperbound -= 1

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
num_sum = 0 
while True:
   message= input("Enter numbers here, or 'exit' to quit:") 
   if message.lower() == 'exit':
       break
   elif message.lstrip('-').isdigit():
        message=int(message)
        num_sum= num_sum+message



print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 
left_term=0
right_term=0 

while True:
    calculate= input("Enter operand operator operand here or 'exit' to quit:")
    if calculate.lower() == 'exit':
        break
    calculate = calculate.replace(" ","")
    operator= None
    operand= []
    for operand in "+-/*%":
        if operand in calculate:
            operands = calculate.split(operand)
            operator = operand

    if operands[0].isdigit() and operands[1].isdigit():
        left_term = int(operands [0])
        right_term = int(operands[1])
    else:
        print(f"Please only enter numerical values")
    
    if operator == '+':
        answer = left_term + right_term
    elif operator == '-':
        answer = left_term - right_term
    elif operator == '/':
        answer = left_term / right_term
    elif operator == '*':
        answer = left_term * right_term
    elif operator == '%':
        answer = left_term % right_term
   
        
    print("Result:", answer)   
        
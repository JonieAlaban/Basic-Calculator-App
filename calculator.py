#Created operation for 2 inputs 
def calculation(n1, operation, n2):
    #Checks inputs are float & coverts string from lines 24 to 25
    try:
        n1 = float(n1)
        n2 = float(n2)
    #Satisfying the conditions depending on user's desired inputs and operation
        if operation == "+":
            result = n1 + n2
        elif operation == "-":
            result = n1 - n2
        elif operation == "/":
            result = n1 / n2
        elif operation == "*":
            result = n1 * n2
        else:
            result = "Syntax Error"
        return result
    #Checks if the user's input is valid or not | if try didn't satisfy the conditions, except will run and display "Invalid Value"
    except ValueError:
        return "Invalid Value"
#These series of codes help user to input the data
n1 = input("Enter first number: ")
n2 = input("Enter second number: ") 
operation = input("Enter operation: ")

#Variable result contains the result of the calculation function 
result = calculation(n1, operation, n2)
#Display the result on the terminal
print("Result:", result)


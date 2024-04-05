num1 = input("Enter number 1: ")
# num2 = input("Enter number 2: ")

try:
    if(num1.isDigit()):
        print(num1)
except Exception as e:
    error_message = str(e)

print(error_message)
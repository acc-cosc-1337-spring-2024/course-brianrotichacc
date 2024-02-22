import repetition
def display_menu():
    print(" Option 1: Factorial\n Option 2: Sum of Odd Numbers\n Option 3: Exit ")

display_menu()
while True:
    homework_3_menu = int(input("Please enter your option: "))
    if homework_3_menu == 1:
        num = int(input("Please enter a number: "))
        if num in range(0,11):
            result = repetition.get_factorial(num)
            print(f"The factorial of {num} is {result}")
        else:
            print("Please enter a number between 1 and 10")
    elif homework_3_menu ==2:
        num = int(input("Please enter a number: "))
        if num in range(0,101): #>=0 and num<=100:
            result = repetition.get_factorial(num)
            print(f"The sum of odd number {num} is {result}")
        else:
            print("Please enter a number between 0 and 100")
    elif homework_3_menu ==3:
        pass
    else:
        print("Please enter a valid choice")
        pass
    keep_going = input("Do you want to continue? (Y/N): ").lower()
    if keep_going != 'y':
        exit()
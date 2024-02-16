import repetition

homework_3_menu = int(input("Please enter your option: "))

if homework_3_menu == 3:
    global keep_going 
    keep_going= input("Do you want to continue? ")
    if keep_going == 'Y' or keep_going == 'y':
        homework_3_menu = int(input("Please enter your option: "))
    else:
        exit()

while keep_going=="Y" or keep_going=="y":
    if homework_3_menu == 1:
        num = int(input("Please enter a number: "))
        if num>=0 and num<=10:
            result = repetition.get_factorial(num)
            print(f"The factorial of {num} is {result}")
        else:
            num = int(input("Please enter a valid number: "))
            result = repetition.get_factorial(num)
            print(f"The factorial of {num} is {result}")
        # keep_going = input("Do you want to Continue? ")
    elif homework_3_menu ==2:
        num = int(input("Please enter a number: "))
        if num>=0 and num<=100:
            result = repetition.get_factorial(num)
            print(f"The factorial of {num} is {result}")
        else:
            num = int(input("Please enter a valid number: "))
            result = repetition.get_factorial(num)
            print(f"The sum of odd numbers of {num} is {result}")
    else:
        print('Invalid Number Entry')
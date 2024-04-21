import class_a as a
def display_menu():
    print(" Option 1: Roll dice\n Option 2: Exit ")

display_menu()
while True:
    homework_9_menu = int(input("Please enter your option: "))
    if homework_9_menu == 1:
        die1 = a.die()
        die1.roll()
        rolled_value = die1.get_rolled_value()
        print(rolled_value)
    elif homework_9_menu ==2:
        exit()
    else:
        print("Please enter a number between 1 and 2")
    
    keep_going = input("Do you want to continue? (Y/N): ").lower()
    if keep_going != 'y':
        exit()
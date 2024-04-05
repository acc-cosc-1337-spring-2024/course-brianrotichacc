#set assignment
import sets
def display_menu():
    print("Selection Menu")
    print(" 1- Student who took prog1 and prog2\n 2- Student who took prog2 only\n 3- Student who took prog1 only\n 4- Student who took prog1 or prog2\n 5- Exit")

display_menu()

prog1 = {'Student1', 'Student2', 'Student3'}
prog2 = {'Student3', 'Student4', 'Student5'}

while True:
    display_menu = int(input("Please enter your option: "))
    if display_menu == 1:
        student_set = sets.get_students_who_took_prog1_and_prog2(prog1, prog2)
        print(student_set)
    elif display_menu == 2:
        student_set = sets.get_students_who_took_prog2_not_prog1(prog1, prog2)
        print(student_set)
    elif display_menu == 3:
        student_set = sets.get_students_who_took_prog1_not_prog2(prog1, prog2)
        print(student_set)
    elif display_menu == 4:
        student_set = sets.get_students_who_took_prog1_or_prog2(prog1, prog2)
        print(student_set)
    elif display_menu == 5:
        exit()
    else: 
        print("Please select a valid choice")

###########################################################################################################################################
# # Dictionary assignment 
# import dictionary
# def display_menu():
#     print("Inventory Menu")
#     print(" 1-Add or Update Item\n 2-Delete Item\n 3-Exit")

# display_menu()
# while True:
#     display_menu = int(input("Please enter your option: "))
#     if display_menu == 1:
#         widget_name = input("Enter a widget Name: ")
#         quantity = int(input("Enter the quantity: "))
#         dictionary.add_inventory(dictionary.inventory,widget_name,quantity)
#     elif display_menu == 2:
#         widget_name = input("Enter Widget Name: ")
#         dictionary.remove_inventory_widget(widget_name)
#     elif display_menu == 3: 
#         exit()
#     else: 
#         pass
#     print(dictionary.inventory)
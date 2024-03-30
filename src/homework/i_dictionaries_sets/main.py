import dictionary
def display_menu():
    print("Inventory Menu")
    print(" 1-Add or Update Item\n 2-Delete Item\n 3-Exit")

display_menu()
while True:
    display_menu = int(input("Please enter your option: "))
    if display_menu == 1:
        widget_name = input("Enter a widget Name: ")
        quantity = int(input("Enter the quantity: "))
        dictionary.add_inventory(dictionary.inventory,widget_name,quantity)
    elif display_menu == 2:
        widget_name = input("Enter Widget Name: ")
        dictionary.remove_inventory_widget(widget_name)
    elif display_menu == 3: 
        exit()
    else: 
        pass
    print(dictionary.inventory)
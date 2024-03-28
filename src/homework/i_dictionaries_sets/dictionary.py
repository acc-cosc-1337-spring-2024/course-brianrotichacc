def add_inventory(widgets, widget_name, quantity):

    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity


inventory = {'widget1': 30, 'widget2': 10}
def remove_inventory_widget(widget_name):

    global inventory
    if widget_name in inventory:
        del inventory[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'

inventory = {'widget1': 30, 'widget2': 10}
remove_inventory_widget('widget1')
print(len(inventory))
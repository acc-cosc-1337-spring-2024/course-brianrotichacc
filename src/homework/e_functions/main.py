import value_return
# set value variable
value = 3800
# Call functions from value return file and pass value parameter 
hour = value_return.get_hour(value)
minute = value_return.get_minutes(value)
second = value_return.get_seconds(value)
# Output program 
print(str('%02d'%hour)+':'+str('%02d'%minute)+':'+str('%02d'%second))

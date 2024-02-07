import decisions
# initialize variables by allowing users to input values from the keyboard and convert it to an integer value
option = int(input("Please enter option value: "))
total = int(input("Please enter total value: "))
# Get the ratio by calling get options ratio function from decision file and assign it to a variable
ratio = decisions.get_options_ratio(option, total)
# get the rating by passing in the assigned ratio value from ratio function and pass it to faculty rating function
rating = decisions.get_faculty_rating(ratio)
# Display the result from the function
print(rating)

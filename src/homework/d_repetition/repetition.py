def get_factorial(num):
    # Initializing variable
    factorial = 1
    # For range loop to calculate factorial
    for i in range(1, num + 1):
        factorial *= i 
    return factorial

def sum_odd_numbers(num):
    # Initialize sum_total variable
    sum_total = 0
    i=1
    while i<=num:
        #Check if the number is odd
        if i%2 != 0:
            #Add odd number to sum_total
            sum_total += i
        i+=1       
    return sum_total
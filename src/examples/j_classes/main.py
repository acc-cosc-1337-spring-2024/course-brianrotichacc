import coin_class
import bank_account


my_coin = coin_class.Coin()

# print('This side is up:', my_coin.get_sideup())

# print("I'm tossing the coin .....", my_coin.toss())

# print('This side is up:', my_coin.get_sideup())


start_bal = float(input('Enter your starting balance: '))

#Create a BankAccount object

savings = bank_account.BankAccount(start_bal)

#deposit the user's paycheck
pay = float(input('How much were you paid this week?'))
print('I will deposit that into your account')
savings.deposit(pay)

#display the balance
print(f'Your current account balance is: ${savings.get_balance():,.2f}')

# get the amount to withdraw

cash = float(input('How much would you like to withdraw? '))
print(f'I will withdraw {cash} from your account')
savings.withdraw(cash)

# display balance 
print(f'Your remaining account balance is: ${savings.get_balance():,.2f}')


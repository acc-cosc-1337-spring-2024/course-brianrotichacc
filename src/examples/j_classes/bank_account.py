# The BankAccount class simulates a bank account

class BankAccount:

    #The __init__ method accepts an argument for the account's balance. it is assigned to the  __balance attribute

    def __init__(self, bal):
        self.__balance = bal

    #The deposit method makes a deposit into the account
        
    def deposit(self, amount):
        self.__balance+=amount

    #The withdraw method withdraws an amount from the account
    
    def withdraw(self, amount):
        if self.__balance >=amount:
            self.__balance-=amount
        else:
            print('You have insufficient funds')

    #get balance method returns the account balance
    
    def get_balance(self):
        return self.__balance
            

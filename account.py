from datetime import datetime
time =  datetime.now()
print(time)
class BankAccount:
    
    def __init__(self,first_name,last_name,phone_number,bank):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.phone_number = phone_number
        self.bank = bank
        self.deposits = []
        self.withdrawals = []
        self.loan=[]

    def account_name(self):
        name ="{} account for {} {}".format(self.bank,self.first_name,self.last_name,self.phone_number)
        return name
        
    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
         
        else:
            self.balance += amount
            self.deposits.append(amount)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("You have deposited {} to {} on {}".format(amount, self.account_name(), formated_time))
            return
    
        
    def get_balance(self):
        return "The balance for {} is {} ".format(self.account_name(),self.balance)
    
    def withdraw(self,amount):
        try:
            amount + 1
        except TypeError:
             print("You must enter the amount in figures")
             return
        if amount <=0:
            print("You can withdraw the money")
        elif amount > self.balance:
            print("You don't have enough money")
        else:
            self.balance -=amount
            self.withdrawals.append(amount)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("You have withdrawn {} to {} on {}".format(amount, self.account_name(), formated_time))
            return

    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
            return

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
            return


    def request_loan(self,amount):
        try:
            amount + 1
        except TypeError:
             print("You must enter the amount in figures")
             return
        if amount <= 0:
            print("You cannot request that amount")
        else:
            self.amount=amount
            print("You have been give a loan of {}".format(amount))
    def repay_amount(self,amount):

        try:
            amount + 1
        except TypeError:
             print("You must enter the amount in figures")
             return 
        
        if amount <= 0:
            print("You can't reapay that amount")
        elif self.loan == 0:
            print("You dont have loan at the momenyt")
        elif amount > self.loan:
            print("You loan is {},Please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            print("You have paid your loan with {}.Your loan balance is {}".format(amount,self.loan))




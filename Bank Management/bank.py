import random


class Account:
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.transaction_history = []
        self.account_no = random.randint(200000,999999)
        self.balance = 0
        self.loan_count = 0

    def deposit(self,amount,bank):
        self.balance += amount
        bank.total_balance += amount
        self.transaction_history.append(f"Deposited amount {amount}")
        print(f"Deposited {amount} to account {self.account_no}")
        bank.check_bankrupt() 

    
    def withdraw(self,amount,bank):
        if bank.is_bankrupt:
            print("The bank is bankrupt, withdrawal not allowed.")
            return
        
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
             self.balance -= amount
             bank.total_balance -= amount
             self.transaction_history.append(f"withdraw amount {amount}")
             print(f"Withdraw {amount} from account {self.account_no}")
             bank.check_bankrupt()
    
    def check_balance(self):
        print(f"Availabe balance: {self.balance}")

    def show_transaction_history(self):
        print("Transaction History: ")
        for transaction in self.transaction_history:
            print(transaction)

        
    def take_loan(self, loan_amount,bank):
        if not bank.loan_status:
            print("Loan feature is turned off.")
            return
           
        if self.loan_count < 2:
            self.balance += loan_amount
            bank.total_loan += loan_amount
            self.loan_count += 1
            bank.total_balance += loan_amount
            self.transaction_history.append(f"Loan Taken: {loan_amount}")
            print(f"Loan of {loan_amount} taken for account {self.account_no}")
        else:
            print("Loan limit exceeded")


    def transfer(self,amount,receiver_account,bank):
        if bank.is_bankrupt:
            print("The bank is bankrupt, transfer not allowed.")
            return
        
        if amount > self.balance:
            print("Transfer amount exceeded")
        elif not receiver_account:
            print("Acoount does not exit")
        else:
            self.balance -= amount
            receiver_account.balance += amount
            bank.total_balance -= amount
            self.transaction_history.append(f"Tansferred {amount} to account {receiver_account.account_no}")
            self.transaction_history.append(f"Received {amount} from account {self.account_no}")
            bank.check_bankrupt()




class Bank:
    def __init__(self):
        self.accounts_list = []
        self.loand_status = True
        self.total_balance = 0
        self.total_loan = 0
        self.is_bankrupt = True

    
    def update_total_balance(self):
        total = 0
        for account in self.accounts_list:
          total += account.balance
          self.total_balance = total

    def create_account(self,name,email,address,account_type):
        account = Account(name,email,address,account_type)
        self.accounts_list.append(account)
        print(f"Account created successfully! Account no: {account.account_no}")


    def delete_account(self,account_no):
        for account in self.accounts_list:
            if account.account_no == account_no:
                self.accounts_list.remove(account)
                self.update_total_balance()
                print(f"Account {account_no} deleted successfully!")
                return 
            
        print("Account not found!")


    def show_users(self):
        if self.accounts_list:
            for account in self.accounts_list:
                print(f"Account no: {account.account_no}\tName: {account.name}\tEmail: {account.email}\tBalance: {account.balance}")
        else:
            print("No users found!")


    def check_bankrupt(self):
        if self.total_balance == 0:
            self.is_bankrupt = True
            print("The bank is bankrupt!")
        else:
            self.is_bankrupt = False
            print(f"Total available balance in the bank: {self.total_balance}")



    def total_loan_amount(self):
          print(f"Total loan amount in the bank: {self.total_loan}")


    def off_loan(self):
        self.loand_status = False
        print("Loan feature turned off !")

    def on_loan(self):
        self.loand_status = True
        print("Loan feature turned on !")

    


bank = Bank()
bank.create_account("Rahim", "rahim@gmail.com", "Khulna", "Savings")
bank.create_account("Karim", "karim@gmail.com", "Dhaka", "Current")


bank.check_bankrupt()


user1 = bank.accounts_list[0]
user2 = bank.accounts_list[1]


user1.deposit(1000, bank)
user1.withdraw(200, bank)
user1.check_balance()

user1.transfer(300, user2, bank)
user1.show_transaction_history()
user2.show_transaction_history()

bank.update_total_balance()
bank.check_bankrupt()

bank.off_loan()
bank.on_loan()








            

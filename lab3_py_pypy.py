class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
    @property
    def get_name(self):
        return self.__name


class Account:
    def __init__(self, account_number: str, owner: User, balance=0):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []
    @property
    def account_number(self):
        return self.__account_number
    @property
    def get_balance(self):
        return self.__balance

    def deposit(self, amount, atm_id):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"D-ATM:{atm_id}-{amount}-{self.__balance}")
            return "Success"
        return "Error: Deposit amount must be greater than 0"

    def withdraw(self, amount, atm_id):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"W-ATM:{atm_id}-{amount}-{self.__balance}")
            return "Success"
        elif amount > self.__balance:
            return "Error: Insufficient funds in account"
        return "Error: Withdrawal amount must be greater than 0"

    def transfer(self, to_account, amount, atm_id):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            to_account.deposit(amount, atm_id)
            self.__transactions.append(f"TD-ATM:{atm_id}-{amount}-{self.__balance}")
            return "Success"
        elif amount > self.__balance:
            return "Error: Insufficient funds in account"
        return "Error: Transfer amount must be greater than 0"
   
    def get_transactions(self):
        return self.__transactions


class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin

    def validate_pin(self, pin):
        return self.__pin == pin
    @property
    def get_account(self):
        return self.__account
    @property
    def get_card_number(self):
        return self.__card_number


class ATMMachine:
    Per_LIMIT = 40000

    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__balance = initial_amount
        self.__daily_withdrawals = {}

    def insert_card(self, card: ATMCard, pin: str):
        if card.validate_pin(pin):
            return card.get_account
        return "Invalid PIN"

    def deposit(self, account: Account, amount):
        if amount > 0:
            account.deposit(amount, self.__machine_id)
            self.__balance += amount
            return "Success"
        return "Error: Deposit amount must be greater than 0"

    def withdraw(self, account: Account, amount):
        if amount > 0:
            daily_withdrawn = self.__daily_withdrawals.get(account, 0)
            if daily_withdrawn + amount > ATMMachine.Per_LIMIT:
                return f"Exceeds per one withdrawal limit of {ATMMachine.Per_LIMIT} baht"
            if self.__balance >= amount:
                result = account.withdraw(amount, self.__machine_id)
                if result == "Success":
                    self.__balance -= amount
                    self.__daily_withdrawals[account] = daily_withdrawn + amount
                return result
            return "Error: ATM has insufficient funds"
        return "Error: Withdrawal amount must be greater than 0"

    def transfer(self, from_account: Account, to_account: Account, amount):
        return from_account.transfer(to_account, amount, self.__machine_id)
    @property
    def get_balance(self):
        return self.__balance


class Bank:
    def __init__(self, users_data, atms_data):
        self.__users = []
        self.__accounts = []
        self.__cards = []
        self.__atms = []

        for citizen_id, data in users_data.items():
            name, account_number, card_number, balance = data
            user = User(citizen_id, name)
            account = Account(account_number, user, balance)
            card = ATMCard(card_number, account, card_number)  # Default PIN
            self.__users.append(user)
            self.__accounts.append(account)
            self.__cards.append(card)

        for atm_id, initial_amount in atms_data.items():
            atm = ATMMachine(atm_id, initial_amount)
            self.__atms.append(atm)

    def get_card_by_number(self, card_number):
        for card in self.__cards:
            if card.get_card_number == card_number:
                print(card.get_card_number)
                return card
        return "Error"

    def get_atm_by_id(self, atm_id):
        for atm in self.__atms:
            if atm._ATMMachine__machine_id == atm_id:
                return atm
        return "Error"
   


# Data initialization
users_data = {
    '1-1101-12345-12-0': ['Harry Potter', '1234567890', '12345', 20000],
    '1-1101-12345-13-0': ['Hermione Jean Granger', '0987654321', '12346', 1000],
}
atms_data = {'1001': 1000000, '1002': 200000}
bank = Bank(users_data, atms_data)

atm_machine_1 = bank.get_atm_by_id('1001')
card_harry = bank.get_card_by_number('12345')

print("\nTest Case #1") 
account_harry = atm_machine_1.insert_card(card_harry, '12345')
print(f"Account Number: {account_harry.account_number}") 
print(f"ATM Card Number: {card_harry.get_card_number}")  

print("\nTest Case #2") 
atm_machine_2 = bank.get_atm_by_id('1002')
card_hermione = bank.get_card_by_number('12346')
account_hermione = atm_machine_2.insert_card(card_hermione, '12346')
print(f"Hermione account before test: {account_hermione.get_balance}")  
result = atm_machine_2.deposit(account_hermione, 1000) 
print(f"Hermione account after test: {account_hermione.get_balance}")  
print("Transaction:", account_hermione.get_transactions())  

print("\nTest Case #3")
result = atm_machine_2.deposit(account_hermione, -1)  
print(result)  
print("\nTest Case #4") 
# Before withdrawal
print(f"Hermione account before test: {account_hermione.get_balance}")  
result = atm_machine_2.withdraw(account_hermione, 500)  
print(f"Hermione account after test: {account_hermione.get_balance}")  
print("Transaction:", account_hermione.get_transactions())  
print("\nTest Case #5") 
result = atm_machine_2.withdraw(account_hermione, 2000)  
print(result) 
print("\nTest Case #6") 
account_harry = bank.get_atm_by_id('1001').insert_card(card_harry, '12345')

# Before transfer
print(f"Harry account before test: {account_harry.get_balance}")  
print(f"Hermione account before test: {account_hermione.get_balance}")  

# Transfer 10000 from Harry to Hermione
result = atm_machine_2.transfer(account_harry, account_hermione, 10000)
print(f"Harry account after test: {account_harry.get_balance}")  
print(f"Hermione account after test: {account_hermione.get_balance}")  
print("Transaction:", account_harry.get_transactions())  
print("Transaction:", account_hermione.get_transactions())  

# print("\nTest Case #7") 
print("Hermione transaction history:")
for transaction in account_hermione.get_transactions():
    print(transaction)
print("\nTest Case #8") 
result = atm_machine_1.insert_card(card_harry, '9999') 
print(result)  
print("\nTest Case #9") 
atm_machine_1 = bank.get_atm_by_id('1001')
account_harry = atm_machine_1.insert_card(card_harry, '12345')

# Before withdrawal
print(f"Harry account before test: {account_harry.get_balance}") 
print("Attempting to withdraw 45000 baht...")
result = atm_machine_1.withdraw(account_harry, 45000)
print(f"Expected result: Exceeds per_one withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account_harry.get_balance}")  
print("\nTest Case #10") 
atm_machine_2 = bank.get_atm_by_id('1002')
account_harry = atm_machine_2.insert_card(card_harry, '12345')

# Before withdrawal
print(f"ATM machine balance before: {atm_machine_2.get_balance}")  
print("Attempting to withdraw 250000 baht...")
result = atm_machine_2.withdraw(account_harry, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine_2.get_balance}")  

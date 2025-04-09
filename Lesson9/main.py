class BankAccount:
    __num_transactions = 0 #class variable
    def __init__(self,name,number,balance):
        self.name = name
        self.number = number
        self.__balance = balance

    def get_balance(self):
        return f"${self.__balance:.2f}"
    
    def get_num_transactions(self):
        return BankAccount.__num_transactions

    def set_balance(self, amount):
        if (amount > self.__balance):
            self.__balance = amount
            BankAccount.__num_transactions += 1

def main():
    my_account = BankAccount("Henry Hall-Brown", 1234, 50)
    print(my_account.get_balance())
    print(my_account.get_num_transactions())
    my_account.set_balance(100)
    print(my_account.get_balance())
    print(my_account.get_num_transactions())

if __name__ == "__main__":
    main()
class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance -= amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
            file.close()


class Checking(Account):
    """This is Checking Account Object"""
    type = "checking"
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= amount + self.fee


checking = Checking("balance.txt", 1)
checking.transfer(100)
checking.commit()
print (checking.type)
print (checking.__doc__)
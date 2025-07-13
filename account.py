acc_num = [123456789,234567890,345678901,456789012]
class account:
    def __init__(self,name,account_no,balance,):
        self.balance = balance
        self.account_no = account_no
        self.name = name

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def widraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -=amount
            return self.balance
    def check_balance(self):
        return self.balance

accounts = [
    account("Akash",123456789,90000),
    account("Tumpa",234567890,80000),
    account("Ashis",345678901,70000),
    account("me",456789012,60000)
]

num = int(input("Enter your account number: "))
for i in range(len(acc_num)):
    if acc_num[i] == num:
        user = accounts[i]
        print("Welcome to your account",user.name)
        amount = int(input("Enter the amount you want to deposit: "))
        user.deposit(amount)
        print("Now your updated balance is =",user.check_balance())
        amount = int(input("Enter the amount you want to withdraw: "))
        user.widraw(amount)
        print("Rs",amount,"has been withdrawn.","Now your balance is =",user.check_balance())
        break

else:
    print("Invalid account number")





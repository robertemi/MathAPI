from BankAccount import BankAccount

def main():
    ba = BankAccount(1000)

    print(ba.balance)
    ba.balance = 2000
    ba.withdraw(1000)
    ba.deposit(1000)
    print(ba.balance)

main()
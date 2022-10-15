class Checking_account(object):

    count = 0

    def __init__(self, number, balance):
        self.summa = None
        print("Add new bank balance!")
        self.number = number
        self.balance = int(balance)
        Checking_account.count += 1

    def withdraw(self, summa):
        self.summa = summa


def main():
    bank1 = Checking_account("1234 5678 9123 4567", input("Your balance: "))
    print(bank1.number)
    bank1.summa = int(input("Your Summa: "))
    print(bank1.balance - bank1.summa)


if __name__ == '__main__':
    main()

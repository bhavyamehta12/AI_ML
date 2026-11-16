
class MaxLimitExceeded(Exception):
    pass

class HDFC:

    def __init__(self):
        self.__max_transaction = 3
        self.__max_withdrawal = 20000
        self.__transactions_used = 0

    def withdraw(self, amount):

        if self.__transactions_used >= self.__max_transaction:
            raise MaxLimitExceeded("HDFC: Maximum transaction limit exceeded!")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > self.__max_withdrawal:
            raise MaxLimitExceeded("HDFC: Maximum withdrawal limit is Rs. 20,000")
        
        self.__transactions_used += 1

        print("HDFC: Withdrawal Successful!")
        print("Amount Withdrawn:", amount)
        print("Transactions Remaining:",
              self.__max_transaction - self.__transactions_used)
class AXIS:

    def __init__(self):
        self.__max_transaction = 5
        self.__max_withdrawal = 30000
        self.__transactions_used = 0

    def withdraw(self, amount):
        if self.__transactions_used >= self.__max_transaction:
            raise MaxLimitExceeded("AXIS: Maximum transaction limit exceeded!")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > self.__max_withdrawal:
            raise MaxLimitExceeded("AXIS: Maximum withdrawal limit is Rs. 30,000")
        self.__transactions_used += 1

        print("AXIS: Withdrawal Successful!")
        print("Amount Withdrawn:", amount)
        print("Transactions Remaining:",
              self.__max_transaction - self.__transactions_used)

class ATM:

    def inputAmount(self):
        while True:
            bank = input("Choose Bank (HDFC/AXIS): ").strip().upper()

            if bank == "HDFC":
                bank_obj = HDFC()
                break
            elif bank == "AXIS":
                bank_obj = AXIS()
                break
            else:
                print("Invalid Bank Selection. Try Again.")

        while True:
            try:
                amount = int(input("Enter Withdrawal Amount: "))
                bank_obj.withdraw(amount)

            except MaxLimitExceeded as e:
                print("\nTransaction Terminated!")
                print(e)
                break

            except ValueError as e:
                print("Invalid Input:", e)
                continue

            while True:
                transaction = input(
                    "Want To Do Another Transaction (YES/NO): "
                ).strip().upper()

                if transaction == "YES":
                    break

                elif transaction == "NO":
                    print("Thank you for using ATM!")
                    return

                else:
                    print("Please enter YES or NO.")

        print("ATM Session Closed.")

atm = ATM()
atm.inputAmount()

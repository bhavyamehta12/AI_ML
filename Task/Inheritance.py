import random


class BankInfo:
    def __init__(self, fn, ln, gender, address):
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address


class BankAccount:
    account_numbers = set()

    def __init__(self, amount, object_bank_info):
        self.acno = self.generate_account_number()
        self.amount = amount
        self.object_bank_info = object_bank_info

    @classmethod
    def generate_account_number(cls):
        while True:
            acno = random.randint(1000000000000, 9999999999999)
            if acno not in cls.account_numbers:
                cls.account_numbers.add(acno)
                return acno

    def display_profile(self):
        print("\n----- Bank Account Profile -----")
        print("First Name:", self.object_bank_info.fn)
        print("Last Name:", self.object_bank_info.ln)
        print("Gender:", self.object_bank_info.gender)
        print("Address:", self.object_bank_info.address)
        print("Account Number:", self.acno)
        print("Amount:", self.amount)


class Saving(BankAccount):
    min_amount = 10000
    rate = 6

    def __init__(self, amount, object_bank_info, months):
        super().__init__(amount, object_bank_info)
        self.months = months

    def calculate_interest(self):
        return (self.amount * self.rate * self.months) / (100 * 12)

    def display_profile(self):
        super().display_profile()
        print("Months:", self.months)
        print("Rate of Interest:", self.rate, "%")
        print("Interest:", self.calculate_interest())


class Current(BankAccount):
    min_amount = 5000
    rate = None


class Main:
    @staticmethod
    def run():
        fn = input("Enter First Name: ")
        ln = input("Enter Last Name: ")
        gender = input("Enter Gender: ")
        address = input("Enter Address: ")

        bank_info_obj = BankInfo(fn, ln, gender, address)

        amount_input = input("Enter Amount: ")

        while True:
            choice = input("Select Account Type (Saving/Current): ").lower()

            if choice == "saving":
                account_type = Saving
                break
            elif choice == "current":
                account_type = Current
                break
            else:
                print("Invalid Account Type")

        for attempt in range(3):
            try:
                amount = float(amount_input)
            except ValueError:
                print("Please Enter a Valid Amount")
            else:
                if amount >= account_type.min_amount:
                    break
                print("Minimum Amount Required:", account_type.min_amount)

            if attempt < 2:
                amount_input = input("Enter Amount Again: ")
        else:
            print("Maximum Attempts Exceeded. Exiting Program.")
            return

        if account_type == Saving:
            months = int(input("Enter Number of Months: "))
            account = Saving(amount, bank_info_obj, months)
        else:
            account = Current(amount, bank_info_obj)

        account.display_profile()


Main.run()
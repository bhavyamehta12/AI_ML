class Account:
    def __init__(self,holder_name,id,balance,status):
        self.holder_name=holder_name
        self.__id=id
        self.balance=balance
        self.status=status
    @property
    def id(self):
        return self.id
    @id.setter
    def id(self,deposit,withdraw):
        if not isinstance(deposit,(int,float)) or not isinstance(withdraw(int,float)):
            raise ValueError("Invalid Input")
        if deposit<=0 or withdraw<=0:
            raise ValueError("Invalid Input")

class TransactionLogger:
    def __init__(self,holder_name,id,balance,status):
        super().__init__(holder_name,id,balance,status)
class BankAccount:
    def __init__(self,holder_name,id,balance,status):
        super().__init__(holder_name,id,balance,status)
class SavingsAccount:
    def __init__(self,holder_name,id,balance,status):
        super().__init__(holder_name,id,balance,status)
class CurrentAccount:
    def __init__(self,holder_name,id,balance,status):
        super().__init__(holder_name,id,balance,status)
class PremiumSavingsAccount:
    def __init__(self,holder_name,id,balance,status):
        super().__init__(holder_name,id,balance,status)
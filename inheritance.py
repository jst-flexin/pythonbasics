class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES sent to {recipient} successfully")
        else:
            print("Insufficient Funds to complete transfer")

class personalmpesa(Mpesa):
        def __init__(self, account_balance, phone_number, ID_number):
             super().__init__(account_balance, phone_number)
             self.ID_number = ID_number

        def buy_airtime(self, amount):
            self.account_balance -= amount

            print(f"{amount} KES AIRTIME bought succcessfully")

class buisinessmpesa(Mpesa):
        def __init__(self, account_balance, phone_number, business_name):
            super().__init__(account_balance, phone_number)
            self.business_name = business_name
        def receive_payment(self,amount):
            self.account_balance -= amount
            print(f"{amount} KES received from a customer.")

personal = personalmpesa(30000,721129199,26575358)
personal.send_money(3000, 721129199)

business = buisinessmpesa(16000,732642878,24354678)
business.receive_payment(16000)

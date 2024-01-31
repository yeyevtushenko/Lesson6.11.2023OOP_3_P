class ElectronicWallet:
    def __init__(self, initial_balance=0.0):
        self.__balance = initial_balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"До гаманця додано {amount} грн. Новий баланс: {self.__balance} грн.")
        else:
            print("Сума повинна бути більше 0.")

    def withdraw_money(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"З гаманця знято {amount} грн. Новий баланс: {self.__balance} грн.")
        elif amount <= 0:
            print("Сума повинна бути більше 0.")
        else:
            print("Недостатньо коштів на балансі.")

    def check_balance(self):
        print(f"Поточний баланс гаманця: {self.__balance} грн.")


wallet = ElectronicWallet()

added_amount = float(input("Введіть суму для додавання до гаманця: "))
wallet.add_money(added_amount)

withdrawn_amount = float(input("Введіть суму для зняття з гаманця: "))
wallet.withdraw_money(withdrawn_amount)


wallet.check_balance()
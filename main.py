class BankAccount:
    def __init__(self, owner, card_number, pin, balance=0):
        self.owner = owner
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.blocked = False

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def show_balance(self):
        if self.blocked:
            return "Karta bloklangan!"
        return f"Balans: {self.balance} so'm"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} so'm qo'shildi"
        return "Xato summa!"

    def withdraw(self, amount):
        if self.blocked:
            return "Karta bloklangan!"
        if amount > self.balance:
            return "Yetarli mablag' yo‘q"
        self.balance -= amount
        return f"{amount} so'm yechildi"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "PIN muvaffaqiyatli o‘zgartirildi"
        return "Eski PIN noto‘g‘ri"

account = BankAccount("Jahongir", "8600123412341234", 1234, 500000)
print(account.show_balance())
print(account.deposit(200000))
print(account.withdraw(100000))
print(account.change_pin(1234, 4321))

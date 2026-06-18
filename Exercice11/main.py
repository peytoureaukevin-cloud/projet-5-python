class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Le montant du dépôt doit être positif.")
            return False

        self.balance += amount
        print(f"Dépôt de {amount} effectué.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Le montant du retrait doit être positif.")
            return False

        if amount > self.balance:
            print("Solde insuffisant.")
            return False

        self.balance -= amount
        print(f"Retrait de {amount} effectué.")
        return True

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}")
        print(f"Solde : {self.balance}")

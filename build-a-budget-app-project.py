class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __repr__(self):
        output = []

        stars = '*' * int((30 - len(self.name)) / 2)
        output.append(f"{stars}{self.name}{stars}")
        for amount, description in (d.values() for d in self.ledger):
            amount = "{:.2f}".format(amount)
            if len(description) > (30 - len(str(amount)) - 1):
                description = description[:29 - len(str(amount))]
            output.append(f"{description}{' ' * (29-len(description)-len(str(amount)))} {amount}")

        output.append(f"Total: {self.balance}")
        return "\n".join(output)

    def check_funds(self, amount):
        return True if self.get_balance() - amount >= 0 else False

    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.withdraw(amount,f"Transfer to {category.name}"):
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
    

def create_spend_chart(categories):
    spent_amounts = [
        round(sum(abs(item["amount"]) for item in category.ledger if item["amount"] < 0), 2)
        for category in categories
    ]

    total = round(sum(spent_amounts), 2)
    percentages = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))
    
    graph = "Percentage spent by category\n"
    for val in range(100,-1,-10):
        graph += str(val).rjust(3)+"|"
        for percent in percentages:
            graph += " o " if percent >= val else "   "
        graph += " \n"
    
    x_axis = '-' * (len(categories) * 3 + 1)
    graph += '    ' + x_axis

    names = list(map(lambda x: x.name,categories))
    max_length = max(map(len,names))
    names = list(map(lambda x: x.ljust(max_length,' '),names))
    names = [[f" {names[j][i]} " for j in range(len(names))] for i in range(len(names[0]))]

    graph += '\n    ' + '\n    '.join([''.join(row)+' ' for row in names])
    return graph


food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(13.60, "jacket")
print(food,'\n')
print(clothing,'\n')

create_spend_chart([food,clothing])

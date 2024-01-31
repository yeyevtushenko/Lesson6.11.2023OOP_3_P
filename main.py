class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self):
        product = input("Введіть назву товару: ")
        price = float(input("Введіть вартість товару за одиницю: "))
        quantity = int(input("Введіть кількість одиниць товару: "))

        if quantity <= 0:
            print("Кількість товару повинна бути більше 0.")
            return

        if product in self.__items:
            self.__items[product]["quantity"] += quantity
        else:
            self.__items[product] = {"price": price, "quantity": quantity}

    def calculate_total(self):
        total = sum(item["price"] * item["quantity"] for item in self.__items.values())
        return total

    def display_cart(self):
        print("Зміст кошика:")
        for product, details in self.__items.items():
            print(f"{product}: {details['quantity']} шт. за {details['price']} грн кожен")


cart = ShoppingCart()

cart.add_item()
cart.add_item()
cart.add_item()

total_cost = cart.calculate_total()
print(f"\nЗагальна вартість покупок: {total_cost} грн\n")

cart.display_cart()

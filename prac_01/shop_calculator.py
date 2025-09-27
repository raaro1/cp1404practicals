"""Calculates the total price of items including discounted prices"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > 100:
    discounted_price = total_price * 0.10
    total_price -= discounted_price

print(f"Total price for {number_of_items} is ${total_price:.2f}")
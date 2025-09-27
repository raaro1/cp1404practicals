"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOWEST_BONUS = 0.10
HIGHEST_BONUS = 0.15
bonus = 0

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * LOWEST_BONUS

elif sales >= 1000:
    bonus = sales * HIGHEST_BONUS


print(f"Bonus: ${bonus:.2f}")

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
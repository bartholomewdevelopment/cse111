import datetime
current_date = datetime.datetime.now()
print(current_date)

today = current_date.isoweekday()
print(today)

discount = 0
discount_subtotal = 0

subtotal = int(input("Please enter the price of your item: $"))
if (today == 2 or today == 3) and subtotal >= 50:
    discount_subtotal = subtotal * .10
    subtotal -= discount_subtotal
discount = subtotal - discount_subtotal
tax = 1.06
total = subtotal * tax

print(f"Your total discount is ${discount_subtotal:.2f}.")
print()
print(f"Your subtotal is ${subtotal:.2f}.")
print()
print(f"Your tax is ${total - subtotal:.2f}")
print()
print(f"Your total price is ${total:.2f}")
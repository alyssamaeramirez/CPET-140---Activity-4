total = 0
items = 0

price = float(input("Price (0 to stop): "))

while price != 0:
    total += price
    items += 1
    price = float(input("Price (0 to stop): "))

print(f"Items: {items} Total: {total:.2f}")

if items > 0:
    average = total / items
    print(f"Average: {average:.2f}")
else:
    print("Average: 0.00")
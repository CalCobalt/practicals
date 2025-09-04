kinds = int(input("Enter number of kinds of items: "))
total = 0.00
for i in range(1, kinds + 1):
    price, count = input("Enter price and count: ").split()
    price = float(price)
    count = int(count)
    total += price * count
if total >= 100:
    total = total * 0.9
    print("10% discount applied!")
print("Total price is:", '%.2f'%total)
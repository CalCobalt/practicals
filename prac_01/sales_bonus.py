"""
Program to calculate and display a user's bonus base donsales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

while True:
    sales = float(input("Enter sales amount:"))
    if 0 <= sales < 1000:
        bonus = sales * 0.1
        print("Your bonus is:", '%.2f'%bonus)
    elif sales >= 1000:
        bonus = sales * 0.15
        print("Your bonus is:", '%.2f'%bonus)
    else:
        print("Invalid input.")
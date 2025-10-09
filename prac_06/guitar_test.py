# guitar_test.py
from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 500)

current_year = 2025

print(f"{gibson.name} get_age()- Expected 98. Got {gibson.get_age(current_year)}")
print(f"{another.name} get_age()- Expected 7. Got {another.get_age(current_year)}")

print(f"{gibson.name} is_vintage()- Expected True. Got {gibson.is_vintage(current_year)}")
print(f"{another.name} is_vintage()- Expected False. Got {another.is_vintage(current_year)}")

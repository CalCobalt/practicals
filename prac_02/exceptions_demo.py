"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError occurs when the input for numerator or denominator cannot be converted to an integer (e.g., if the user types letters or symbols instead of a number).
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError occurs when the denominator entered is 0, since dividing by zero is not allowed.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes. i can avoid a ZeroDivisionError by checking if the denominator is zero before performing the division, and asking the user to re-enter a valid value if it is.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

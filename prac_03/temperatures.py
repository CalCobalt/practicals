"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit): 
    return 5 / 9 * (fahrenheit - 32)

def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fharenheit: "))
            print("Result: {:.2f} C".format(fahrenheit_to_celsius(fahrenheit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
stored_name = in_file.read().strip()
in_file.close()
print(f"Your name is {stored_name}")

numbers_file = open("numbers.txt", "r")
num1 = int(numbers_file.readline())
num2 = int(numbers_file.readline())
print(num1 + num2)  # expected: 59
total = 0
for line in numbers_file:
    total += int(line)
numbers_file.close()
print(total)
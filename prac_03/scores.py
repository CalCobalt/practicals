import random

def score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    elif score < 50:
        return "Bad"

def main():
    count = int(input("How many scores? "))

    fout = open("./prac_03/results.txt", "w")
    for i in range(count):
        score = random.randint(0, 100)
        result = score_status(score)
        fout.write(f"{score} is {result}\n")
    fout.close()

    print(f"{count} results written to ./prac_03/results.txt")

main()

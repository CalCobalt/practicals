"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
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
    score = float(input("Enter score: "))
    print(score_status(score))
    
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f} -> {score_status(random_score)}")
    

main()
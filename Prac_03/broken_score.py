"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))

    score = random.randint(0, 100)
    print(determine_score(score))


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    else:
        if 90 > score >= 50:
            return "Passable"
        if 100 >= score >= 90:
            return "Excellent"
        if score < 50:
            return "Bad"


main()





# Module 7
#   Programming Assignment 10
#     Prob-1.py

# <Tyler Johnson>

def main():
    sum = 0.0
    x = float(input("Enter a number (negative to quit) >>"))
    while x >=0.0:
        sum = sum + x
        x = float(input("Enter a number (negative to quit) >>"))
    print("The sum of numbers =",sum)
main()    
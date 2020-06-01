# Module 7
#   Programming Assignment 10
#     Prob-3.py

# <Tyler Johnson>

def main():
    
    
    number = -1
    while number <0.0:
        x = float(input("Enter a positive number to begin program: "))
        if x >= 0.0:
            break
    
    sum = 0.0 
    while True:
        x = float(input("Enter a positive number to be added (negative to quit): "))
        if x >= 0.0:
            sum = sum + x
        else:   
            break
         
    print("This is the sum of numbers enterered: ",sum)

main()    
import math


def smallest_multiple():    
    for num in range(1,math.factorial(20)):
        isDivisible = True
        for val in range(1,20):
            isDivisible = isDivisible and num % val == 0
            if not isDivisible:
                break;
        if isDivisible:
            return num

if __name__ == "__main__":
    print(f"{smallest_multiple()}")

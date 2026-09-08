import mymath

number=int(input("enter the number"))
print(f"{number}! = {mymath.factorial_recursive(number)}")
print(f"{number}! = {mymath.factorial_iterative(number)}")
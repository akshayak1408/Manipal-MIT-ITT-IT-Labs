def sumn(n):
    if n <= 0:
        return 0
    else:
        return n + sumn(n - 1)
n = int(input("enter a number"))
result = sumn(n)
print("Sum of first", n, "natural numbers is:", result)

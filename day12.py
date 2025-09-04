n = int(input("Enter N: "))

def rec(k):
    if k > 0:
        print("Hello Recursion")
        rec(k-1)

rec(n)

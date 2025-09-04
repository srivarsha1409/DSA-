def print_reverse(n):
    if n == 0:   # base case
        return
    print(n)
    print_reverse(n-1)

# Example usage
num = int(input("Enter N: "))
print_reverse(num)

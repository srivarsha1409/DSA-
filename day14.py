def print_numbers(n):
    if n == 0:
        return
    print_numbers(n-1)
    print(n)


num = int(input("Enter N: "))
print_numbers(num)

#palindrome
num = 12321
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10


if original == reverse:
    print("Palindrome")
else:
    print("NOT  Palindrome")



#GCD
a = 5
b = 6

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD/HCF is:", gcd)

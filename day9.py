num = 9474
power = len(str(num))   
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("NOT Armstrong number")


#print divisors
num =12
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

#count digits
num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10   

print("Number of digits:", count)



#reverse number:
num = 12345
r = 0

while num > 0:
    digit = num % 10          
    r = r * 10 + digit
    num //= 10                

print("Reversed number:", r)

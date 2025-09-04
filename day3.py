#array
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]

print(f"Original list: {my_list}")
print(f"Reversed list: {reversed_list}")

#strings

my_string = "hello"
reversed_string = ""
for char in my_string:
    reversed_string = char + reversed_string

print(f"Original: {my_string}")
print(f"Reversed: {reversed_string}")
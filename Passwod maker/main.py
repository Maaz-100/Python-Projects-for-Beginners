import random

length = int(input("whats the length of the password"))

special_character = False
while True:
    use_char = input("Do you want to use special char y or n ").lower()
    if use_char == "y" or "n":
        break
if use_char == "y":
    special_character = True

num = False
while True:
    use_num = input("Do you want to use numbers y or n ").lower()
    if use_num == "y" or "n":
        break
if use_num == "y":
    num = True

upper = False
while True:
    use_upper = input("Do you want to use upper case y or n ").lower()
    if use_upper == "y" or "n":
        break
if use_upper == "y":
    upper = True

# 97 to 122 for normal lowercase
# 48 to 57 is nums
# 65 to 90 upper
# 33  46 are char


password_string = ""
lower_case = length

if upper == True:
    lower_case = lower_case - 1
    password_string += chr(random.randint(65,90))

if special_character == True:
    lower_case = lower_case - 1
    password_string += chr(random.randint(33,46))

if num == True:
    lower_case = lower_case - 1
    password_string += chr(random.randint(48,57))


for i in range(lower_case):
    password_string += chr(random.randint(97,122))

print(password_string)

#could of used random.choice sting.digit
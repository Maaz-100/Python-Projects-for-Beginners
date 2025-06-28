length = False
upper = False
special = False
numbers = False

password = input("Enter password ")

score = 0

if len(password) > 12:
    score = score + 3
    length = True
elif len(password) > 8:
    score = score + 2

elif len(password) > 4:
    score = score + 1

for char in password:
    if char.isupper():
        upper = True
        score = score + 2

for char in password:
    if char in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
                '}', '~']:

        score = score + 3
        special = True

for char in password:
    if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        score = score + 2
        numbers = True
print("")
print(f"This password got a rating of {score} out of 10")
print("You can improve by your password by ")
print("")

if length == False:
    print("Making your password longer")

if numbers == False:
    print("Include numbers")

if special == False:
    print("Add special charters")

if upper == False:
    print("Add uppercase letters")


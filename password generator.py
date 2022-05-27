import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=,.<>"
number = int(input("number of passwords required: "))
length = int(input("length of password: "))
if number == 1:
    print("here is your generated password")
else:
    print("here are your generated passwords")

for pas in range(number):
    password = ''
    for c in range(length):
        password += random.choice(characters)
    print(password)
    
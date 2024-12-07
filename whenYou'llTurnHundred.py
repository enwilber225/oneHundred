# Elias Wilber
# Ask user for name and age, tell them the year it will be when they turn 100
# 12/07/2024

currentYear = 2024
print()

while True:
    name = input("Hi there! What is your name?: ")

    if name.isalpha() == True:
        break
    else:
        print("You need to type a name with only alphabetical characters. Try again!")
        continue

print()

while True:

    age = input(f"Hi there, {name.title()}!\nFor quality purposes, what's your age?: ")
    
    
    if age.isdigit() == True:
        break
    else: 
        print("Wrong, you need to only enter a digit.")
        continue

age = int(age)
name = name.title()

dif = (100 - age)

ageWhenHundred = (dif + currentYear)
print()
print(f"Okay, so your name is, {name.title()}, and your age is {age}. Thanks for the information.")
print()
print(f"It looks like you will turn 100 in the year {ageWhenHundred}! Live your life and enjoy it.")
print()
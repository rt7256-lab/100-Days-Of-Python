print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("tumhara age kya ahi"))
    if age <= 18:
        print("bache ho tum nhi jhul sakte")
    elif age <= 22:
        print("kya yrr etna hi age hai")
    else:
        print("jhullo be tum young ho")
else:
    print("Sorry you have tto grow taller before you can ride.")
import random

name = ["rayan" , "altaaf hussain" , "akshay kumaar" , "modi" , "hamza" , "asim muneer" , "imraan khan" ]

action = ["currupted" , "cancled" , "danced with" , "eats" , "declared" , "order" , "celebrates at"]

place = ["raheen yawr khan" , "sakkhar" , "pathan court" , "karachi" , "lahore" , "peshawar" , "mountains" ]



while True:
    names = random.choice(name)
    actions = random.choice(action)
    places = random.choice(place)

    headline =f"Breaking News {names} {actions} {places}"
    print(headline)

    userinput = input("do you wanted more news yes/no =" ).strip().lower()

    if userinput == "no":
        break

print("thanks for being with us")

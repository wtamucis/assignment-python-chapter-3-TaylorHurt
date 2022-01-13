# Follow the assignment instructions to code an app that
# will tell a user their birthstone.
# Task E
user_input = "Enter the number of the month you were born (1-12) "
output = "Your birthstone is "
month = int(input(user_input))
if month == 1:
    print(output + "garnet.")
elif month == 2:
    print(output + "amethyst.")
elif month == 3:
    print(output + "aquamarine.")
elif month == 4:
    print(output + "diamond.")
elif month == 5:
    print(output + "emerald.")
elif month == 6:
    print(output + "alexandrite.")
elif month == 7:
    print(output + "ruby.")
elif month == 8:
    print(output + "peridot.")
elif month == 9:
    print(output + "sapphire.")
elif month == 10:
    print(output + "pink tourmaline.")
elif month == 11:
    print(output + "topaz.")
elif month == 12:
    print(output + "blue topaz.")
print("*" * 30)

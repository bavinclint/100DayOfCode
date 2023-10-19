print("Welcome to Treasure Island.\nYour missinon is to find the treasure.")
cross_road = input(
    "You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if cross_road == "left":
    lake = input("wait or swim\n")
    if lake == "wait":
        island = input("red yellow or blue")
else:
    print("It's a room full of fire. Game Over")

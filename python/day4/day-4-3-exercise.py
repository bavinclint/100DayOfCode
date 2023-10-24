# Treasure map
row1 = ["⬜️", "⬜️", "⬜️",]
row2 = ["⬜️", "⬜️", "⬜️",]
row3 = ["⬜️", "⬜️", "⬜️",]

mapp = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

mapp[vertical][horizontal] = 'X'


print(f"{row1}\n{row2}\n{row3}")

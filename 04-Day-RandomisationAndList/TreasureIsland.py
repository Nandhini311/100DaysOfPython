'''You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list.'''

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x = (int(position[0])-1)
y = (int(position[1])-1)

map = [row1,row2,row3]
map[x][y] = "x"

print(f"{row1}\n{row2}\n{row3}")

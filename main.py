line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("enter the input, Where do you want to put the treasure? ") 


if position[0] == 'A':
  if position[1] == '1':
    map[0][0] = "X"
  if position[1] == '2':
    map[1][0] = "X"
  if position[1] == '3':
    map[2][0] = "X"

if position[0] == 'B':
  if position[1] == '1':
    map[0][1] = "X"
  if position[1] == '2':
    map[1][1] = "X"
  if position[1] == '3':
    map[2][1] = "X"

if position[0] == 'C':
  if position[1] == '1':
    map[0][2] = "X"
  if position[1] == '2':
    map[1][2] = "X"
  if position[1] == '3':
    map[2][2] = "X"

print(f"{line1}\n{line2}\n{line3}")

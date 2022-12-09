with open("input.txt", "r") as input:
  input_lines = input.readlines()
    
# Part One
positions = set()

hx, hy = 0, 0
tx, ty = 0, 0

for line in input_lines:
  dir, steps = line.split()

  for i in range(int(steps)):
    if dir == "U":
      hy += 1
    if dir == "D":
      hy -= 1
    if dir == "L":
      hx -= 1
    if dir == "R":
      hx += 1

    if (abs(hy - ty) > 1 and abs(hx - tx) == 1):
      if hy - ty > 0:
        ty = hy - 1
        tx = hx
      if hy - ty < 0:
        ty = hy + 1
        tx = hx
    elif (abs(hy - ty) == 1 and abs(hx - tx) > 1):
      if hx - tx > 0:
        tx = hx - 1
        ty = hy
      if hx - tx < 0:
        tx = hx + 1
        ty = hy
    elif abs(hy - ty) > 1:
      if hy - ty > 0:
        ty = hy - 1
      if hy - ty < 0:
        ty = hy + 1
    elif abs(hx - tx) > 1:
      if hx - tx > 0:
        tx = hx - 1
      if hx - tx < 0:
        tx = hx + 1

    positions.add((tx, ty))

part_one = len(positions)

positions = set()

# Part Two
hx, hy = 0, 0
tx, ty = 0, 0

for line in input_lines:
  dir, steps = line.split()

  for i in range(int(steps)):
    if dir == "U":
      hy += 1
    if dir == "D":
      hy -= 1
    if dir == "L":
      hx -= 1
    if dir == "R":
      hx += 1

part_two = len(positions)

print("Part One: {}".format(part_one))
print("Part Two: {}".format(part_two))


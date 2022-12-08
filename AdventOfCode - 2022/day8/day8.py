from functools import reduce

with open("input.txt", "r") as input:
  grid = []
  input_lines = input.readlines()

  for line in input_lines:
    grid.append([*line.strip("\n")])

part_one = 0

for i in range(len(grid)):
  for j in range(len(grid)):
    left_right = grid[i]
    up_down = []

    for t in range(len(grid)):
      up_down.append(grid[t][j])

    visibilites = 4

    # right
    for t in range(j + 1, len(grid)):
      if int(grid[i][j]) <= int(left_right[t]):
        visibilites -= 1
        break

    # left
    for t in range(j):
      if int(grid[i][j]) <= int(left_right[t]):
        visibilites -= 1
        break

    # down
    for t in range(i + 1, len(grid)):
      if int(grid[i][j]) <= int(up_down[t]):
        visibilites -= 1
        break

    # up
    for t in range(i):
      if int(grid[i][j]) <= int(up_down[t]):
        visibilites -= 1
        break

    if visibilites > 0:
      part_one += 1

scenic_scores = []

for i in range(len(grid)):
  for j in range(len(grid)):
    left_right = grid[i]
    up_down = []

    for t in range(len(grid)):
      up_down.append(grid[t][j])

    up_down.reverse()

    right_score = 0
    left_score = 0
    down_score = 0
    up_score = 0

    # right
    for t in range(j + 1, len(grid)):
      right_score += 1

      if int(grid[i][j]) <= int(grid[i][t]):
        break

    # left
    for t in range(j - 1, - 1, -1):
      left_score += 1

      if int(grid[i][j]) <= int(grid[i][t]):
        break

    # down
    for t in range(i + 1, len(grid)):
      down_score += 1

      if int(grid[i][j]) <= int(grid[t][j]):
        break

    # up
    for t in range(i - 1, -1, - 1):
      up_score += 1

      if int(grid[i][j]) <= int(grid[t][j]):
        break

    scenic_scores.append(right_score * left_score * down_score * up_score)

part_two = max(scenic_scores)

print("Part One: {}".format(part_one))
print("Part Two: {}".format(part_two))
import copy

stacks = [[], [], [], [], [], [], [], [], []]
procedures = []

with open("input.txt", "r") as input:
  for i, line in enumerate(input):
    if "[" in line:
      a = 0
      for x in range(0, len(line), 4):
        if line[x] == "[": stacks[a].append(line[x+1])
        a += 1

    if i >= 10:
      l = line.split()
      procedures.append((l[1], l[3], l[5]))

for stack in stacks: stack.reverse()

p2_stacks = copy.deepcopy(stacks)

for procedure in procedures:
  amount = int(procedure[0])
  fro = int(procedure[1]) - 1
  to = int(procedure[2]) - 1

  p2_move = []

  for i in range(amount):
    # Part One
    if len(stacks[fro]) > 0:
      stacks[to].append(stacks[fro].pop())

    # Part Two
    if len(p2_stacks[fro]) > 0:
      p2_move.append(p2_stacks[fro].pop())

  p2_move.reverse()

  for s in p2_move: p2_stacks[to].append(s)

p1_top_stacks = ""
p2_top_stacks = ""

for stack in stacks:
  p1_top_stacks += stack[-1]

for stack in p2_stacks:
  p2_top_stacks += stack[-1]

print("Part One: {}".format(p1_top_stacks))
print("Part Two: {}".format(p2_top_stacks))
rugsacks = []
groups = []

with open("input.txt", "r") as input:
  for line in input:
    rugsacks.append((line[:len(line)//2], line[len(line)//2:].strip("\n")))
    groups.append(line.strip("\n"))

groups = [groups[i:i+3] for i in range(0, len(groups), 3)]

sum_priority = 0
sum_group_priority = 0

for sack in rugsacks:
  for char in sack[0]:
    if char in sack[1]:
      sum_priority += ord(char) - 96 if char.islower() else ord(char) - 38
      break

for group in groups:
  for char in group[0]:
    if char in group[1] and char in group[2]:
      sum_group_priority += ord(char) - 96 if char.islower() else ord(char) - 38
      break

print("Sum of priorities: {}".format(sum_priority))
print("Sum of group priorities: {}".format(sum_group_priority))
import numpy as np

assignments = 0
overlap = 0

with open("input.txt", "r") as input:
  for line in input:
    s1 = line.split(",")[0].split("-")
    s2 = line.split(",")[1].strip("\n").split("-")

    a1 = np.arange(int(s1[0]), int(s1[1]) + 1, 1)
    a2 = np.arange(int(s2[0]), int(s2[1]) + 1, 1)

    if (a1[0] in a2 and a1[-1] in a2) or (a2[0] in a1 and a2[-1] in a1):
      assignments += 1

    for num in a1:
      if num in a2:
        overlap += 1
        break

print("Part One: {}".format(assignments))
print("Part Two: {}".format(overlap))
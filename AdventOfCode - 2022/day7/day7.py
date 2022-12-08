with open("input.txt", "r") as input:
  input_lines = input.readlines()

directory = {}
cwd = []

for line in input_lines:
  if "$ cd" in line:
    if ".." in line:
      cwd.pop()
    else:
      cwd.append(line.split()[2])
  elif "dir" not in line and "$ ls" not in line:
    for i in range(1, len(cwd) + 1):
      parent_dirs = "/".join(cwd[:i])
      if parent_dirs not in directory:
        directory[parent_dirs] = int(line.split()[0])
      else:
        directory[parent_dirs] += int(line.split()[0])

print(directory)

part_one = 0

used = 70000000 - directory["/"]
goal = 30000000 - used

part_two_candidates = []

for size in directory.values():
  if size < 100000:
    part_one += size

  if size >= goal:
    part_two_candidates.append(size)

part_two = min(part_two_candidates)

print("Part One: {}".format(part_one))
print("Part Two: {}".format(part_two))
# Part 1
with open("input.txt", "r") as input:
  totals = []
  cur_total = 0

  for line in input:
    if line != "\n":
      cur_total += int(line)
    else:
      totals.append(cur_total)
      cur_total = 0

  max_calories = max(totals)
  print("Elf with most snacks has {} calories".format(max_calories))

# Part 2
totals = sorted(totals, reverse=True)
top_three = sum(totals[0:3])

print("Top three elves have {} calories total".format(top_three))
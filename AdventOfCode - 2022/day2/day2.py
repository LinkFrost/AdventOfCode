rounds = []

with open("input.txt", "r") as input:
  for line in input:
    moves = line.split()
    rounds.append((moves[0], moves[1]))

elf_map = {
  "A": "X",
  "B": "Y",
  "C": "Z"
}

score_map = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

score = 0
p2_score = 0

for round in rounds:
  elf_move = elf_map[round[0]]
  my_move = round[1]

  score += score_map[my_move]

  if my_move == "X":
    if elf_move == "Z":
      score += 6
      p2_score += score_map["Y"]
    if elf_move == "X":
      p2_score += score_map["Z"]
    if elf_move == "Y":
      p2_score += score_map["X"]
  if my_move == "Y":
    if elf_move == "X":
      score += 6
    p2_score += score_map[elf_move] + 3
  if my_move == "Z":
    p2_score += 6
    if elf_move == "Y":
      score += 6
      p2_score += score_map["Z"]
    if elf_move == "X":
      p2_score += score_map["Y"]
    if elf_move == "Z":
      p2_score += score_map["X"]

  if my_move == elf_move:
    score += 3

print("My score is {}".format(score))
print("My new score is {}".format(p2_score))
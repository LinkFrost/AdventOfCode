with open("input.txt", "r") as input:
  buffer = input.read()
  
start_marker = 0
message_marker = 0

for i in range(len(buffer)):
  temp = []

  for j in range(i, i + 4): temp.append(buffer[j])
  
  if len(temp) == len(set(temp)):
    start_marker = i + 4
    break

for i in range(len(buffer)):
  temp = []

  for j in range(i, i + 14): temp.append(buffer[j])
  
  if len(temp) == len(set(temp)):
    message_marker = i + 14
    break

print("Part One: {}".format(start_marker))
print("Part Two: {}".format(message_marker))
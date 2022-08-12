lines = []
with open("[Line]Ruby.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line)

convert_line = []
for line in lines:
    line = line.strip().split(" ")
    time = line[0][:5]
    name = line[0][5:]
    chat = line[1]
    convert_line.append(time + " " + name + ":" + chat)

with open("r3_output.txt", "w") as f:
    for line in convert_line:
        f.write(line + "\n")
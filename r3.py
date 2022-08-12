lines = []
with open("[Line]time_Ruby.txt", "r", encoding="utf-8") as f:
    for line in f:
        lines.append(line)

convert_msg = []
for line in lines:
    line = line.strip().split(" ")
    time = line[0][:5]
    name = line[0][5:]
    msg = line[1]
    convert_msg.append(time + " " + name + ": " + msg)

with open("r3_output.txt", "w") as f:
    for line in convert_msg:
        f.write(line + "\n")


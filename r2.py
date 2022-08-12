# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    word_count_ruby = 0
    sticker_count_ruby = 0
    image_count_ruby = 0
    word_count_joe = 0
    sticker_count_joe = 0
    image_count_joe = 0
    for line in lines:
        s = line.split(" ")
        name = s[1]   
        words = s[2:]
        if name == "Ruby(穎如)":
            if s[2] == "貼圖":
                sticker_count_ruby
            elif s[2] == "圖片":
                image_count_ruby += 1
            else:
                for msg in words:
                    word_count_ruby += len(msg)
        elif name == "JoeCh":   
            if s[2] == "貼圖":
                sticker_count_joe += 1
            elif s[2] == "圖片":
                image_count_joe += 1
            else:
                for msg in words:
                    word_count_joe += len(msg)

    print("Ruby說了", word_count_ruby, "個字" )
    print("Ruby傳了", sticker_count_ruby, "個貼圖，使用了",image_count_ruby, "個圖片")
    print("Joe說了", word_count_joe, "個字")
    print("Joe傳了", sticker_count_joe, "個貼圖，使用了",image_count_ruby, "個圖片")

def write_file(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines = read_file("[Line]Ruby.txt")
    lines = convert(lines) 
    # write_file("output.txt", lines)



main()


with open("paragraph.txt", mode="r") as file:
    all_words = []
    for line in file.readlines():
        words = line.strip().split(" ")
        all_words += words
    unique_words = set(all_words)
    print(len(unique_words))
    print(len(all_words))


    with open("unique_words", mode="w") as write_file:
        for item in sorted(unique_words):
            write_file.write(item)
            write_file.write("\n")


print("finish")
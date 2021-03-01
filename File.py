with open("myText.txt", mode="r") as text:
    for line in text.readlines():
        print(line, end="")



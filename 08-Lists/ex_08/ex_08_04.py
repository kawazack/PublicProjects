name = input("choose the file name: ")
handle = open(name)

word_list = []
for line in handle:
    for word in line.split():
        word_list.append(word)

word_list.sort()

print(word_list)
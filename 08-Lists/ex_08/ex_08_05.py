name = input("choose the file name: ")
handle = open(name)

for line in handle:
    wds=line.split()
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[1])
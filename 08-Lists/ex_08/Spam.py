fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence'):
        print(line)
    else:
        continue

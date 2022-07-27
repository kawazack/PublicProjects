fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
    elif line.find('@uct.ac.za') == -1: 
        continue
    print(line)    
print("##################" + "\n")
print('There were', count, 'subject lines in', fname)


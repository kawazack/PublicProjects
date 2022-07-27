fhand = open('mbox-short.txt')
inp = fhand.read()
inp_normal_output = inp.upper()


print(inp[:100] + "\n")
for i in range(1, 4):
    print("######## ########## ########")
print(inp_normal_output[:100] + '\n')

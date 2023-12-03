
file = open("input.txt","r")
lines = file.readlines()

for i,line in enumerate(lines):
    for j in range(len(line)-1):
        print(i,j,line[j])

    # print(i,line)

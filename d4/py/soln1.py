file = open("input1.txt","r")
lines = file.readlines()
total=0
for line in lines:
    try:
        numbers = line.split(":")[1].split("|")
        match = numbers[0].split(" ")
        mine =  numbers[1].split(" ")
        l=[]
        for item in match:
            try:
                i=int(item)
                l.append(i)
            except:
                continue
        match = l
        l=[]
        for item in mine:
            try:
                i=int(item)
                l.append(i)
            except:
                continue

        mine = l
        count=0
        for i in mine:
            for j in match:
                if i == j:
                    total+=1
        print(total)
    except:
        continue

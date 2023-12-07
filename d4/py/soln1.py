file = open("input1.txt","r")
lines = file.readlines()
total=0
map=[]
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
        
        map.append([match,mine])
        # map.append(match)
    except:
        continue
t=0
mc=[]
for index,item in map:
    match_count = 0;
    for mine in item[1]:
        for match in item[0]:
            if mine == match:
                match_count+=1

    
# for i1 in range(len(map)):
#     end=len(map))
#     while i1 != 
# for 
    # while index > 0:
    #     for i in range(len(map)):
    #         for i1 in range(len(map[0])):
    #             for i2 in range(len(map[1])):
# start 
#   start - end
#       while !not:

        



                    



            

    
     # print("match:",item[0], "mine",item[1])

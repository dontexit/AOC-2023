

def parse_to_list():
    map=[]
    f = open("input.txt","r")
    for index,line in enumerate(f.readlines()):
        v=line.split(":")[1]
        v=v.strip()
        v=v.split(" ")
        nv=''
        for i in v:
            try:
                int(i)
                nv+=i
            except:
                continue
        nv=int(nv)
        if index == 0 or index%2 ==0:
            map.append(nv)
        else:
            prev_v=map[index-1]
            ni = [prev_v,nv]
            map[index-1] = ni
            
        # print(nv,index)
    
        
    f.close()
  
        
    print(map)
    return map
def get_wins(time,r_distance):
    total = 0
    if r_distance==0:
        total+=time
        total+=0
    for i in range(time-1):
        ht=i+1
        rt=time-ht
        dt=ht*rt

        print("hold time:",ht,"runtime",rt,"distance",dt)
        if dt > r_distance:
            print("winning",total)
            total+=1
    
    print(total)
    return total

def total_wins(map):
    ways=1
    for game in map:
            ways*=get_wins(game[0],game[1])
    return ways


all_games =parse_to_list()
t=total_wins(all_games)
print(t)
#

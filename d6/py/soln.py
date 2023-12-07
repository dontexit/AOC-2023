

def parse_to_list():
    map=[]
    f = open("input.txt","r")
    for index,line in enumerate(f.readlines()):
        v=line.split(":")[1]
        v=v.strip()
        v=v.split(" ")
        nv=[]
        for i in v:
            try:
                i=int(i)
                nv.append(i)
            except:
                continue
        if index == 0 or index%2 ==0:
            map.append(nv)
        else:
            for i,v in enumerate(nv):
                mv=map[index-1][i]
                ni = [mv,v]
                map[index-1][i] = ni
            
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
        else:
            if total!=0:
                break
    
    print(total)
    return total

def total_wins(map):
    ways=1
    for games in map:
        for game in games:
            ways*=get_wins(game[0],game[1])
    return ways


all_games =parse_to_list()
t=total_wins(all_games)
print(t)


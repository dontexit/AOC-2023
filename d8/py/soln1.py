def parse():
    f=open("input.txt","r")
    m={}
    n=[]
    data=False
    for i,line in enumerate(f.readlines()):
        if not line.strip():
            data = True
            continue
        if data:
           a = line.strip().split("=")
           k=a[0].strip()
           v1,v2=a[1].strip().split(",")
           v1=v1[1:len(v1)].strip()
           v2=v2[0:len(v2)-1].strip()
           m[k]=[v1,v2]
        else:
            inst=line.strip()
            print("char num",len(inst))
            for i in inst:
                if i == "L":
                    n.append(0)
                if i == "R":
                    n.append(1)
    print(len(n),len(m.keys()))
    
    return [n,m]    

def calclucate(map,instr):
    i=0
    next = instr[0]
    keys = list(map.keys())
    keys=[]
    lim=len(instr)-1
    for k in keys:
        if k[2]=="A":
            keys.append(k)

    c=0
    while True: 
        c+=1
        print("count",c,"\n",i)
        matched = False
        for index,key in enumerate(keys):
            val = map[key][next]
            if val[2] == "Z":
                keys[index]=val
                matched=True
                continue
            else:
                keys[index]=val
                matched=False


        if matched:
            break
            
        # print("i: ",i,"key: ",key,"next: ",next,"val: ",val)
        else:
            # print("in else")
            if i < lim:
                i+=1
            else:
                i=0
            next=instr[i]
            continue
    

d = parse()
print(d[1],d[0]) 
calclucate(d[1],d[0])

    

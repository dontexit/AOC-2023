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
    key = "AAA"

    c=0
    while True: 
        c+=1
        print("count",c,"\n",i)
        # lim=len(instr)-1
        # print("lim",lim)
        # if i > len(instr)-1:
        #         print(i,"greate than ",lim)
        #         i=0 
        # print(key,next,lim,i)
        # if i == 0:
            # break
        val = map[key][next]
        print("i: ",i,"key: ",key,"next: ",next,"val: ",val)
        if val == "ZZZ":
            print("Found Z")
            break
        else:
            print("in else")
            if i < len(instr)-1:
                i+=1
            else:
                i=0
            key = val
            next=instr[i]
            continue
    

d = parse()
print(d[1],d[0]) 
calclucate(d[1],d[0])

    

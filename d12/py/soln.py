def parse():
    f = open("inp.txt", "r")
    m=[]
    for line in f.readlines():
        line = line.strip()
        if(line):
            p=line.split(" ")
            # print(p)
            f=p[0]*5
            s=p[1]*5
            s=s.split(",")
            sn=[]
            for i in range(len(s)):
                try:
                    sn.append(int(s[i]))
                except:
                    continue
            m.append([f,sn])
    return m
def comb_matches(m,c):
    # print("rl:",rl)
    hl=[]
    start=False
    count=0
    # tf={}
    ac=0
    for i in range(len(m)):
        # print("i: ",i)
        cl=m[i]
        if cl=="#":
            if start:
                count+=1
            
            else:
                count+=1
                start=True
                
        if cl=="?" or cl=="." or i==len(m)-1:
                if start:
                    start=False
                    hl.append(count)
                    # print("ac",ac)
                    # print("compre",hl[ac],c[ac])
                    # print("star append",hl,c,count)
                    if  ac < len(c):
                        if count == c[ac]:
                            ac+=1
                            count=0
                        else:
                            return False
                    else:
                        return False
    if len(hl) == len(c):
        for i in range(len(hl)):
            if hl[i] != c[i]:
                return False
        return True



        # print(cl,start,count)
    # print(hl)
    


def get_hole_indices(m):
    hm=[]
    for i in range(len(m)):
        cl=m[i]
        if cl == "?":
            hm.append(i)
    return hm

def fill_holes(m,hp,tf):
    nm=list(m)
    # print("holes to fill",hp)

    for i in range(len(hp)):
        # print(i,hp[i])
        # print(tf[i])
        if tf[i] == 0:
            tf[i]="."
        else:
            tf[i]="#"
        # print("current hole index",hp[i])
        # print("current hole fill",tf)
        nm[hp[i]]=tf[i]
    return nm 
            
def get_combos(combo,rl):
    hl=get_hole_indices(combo)
    n=len(hl)
    matches=0
    for i in range(2 ** n):
        current_combination = []
        for j in range(n):
            current_combination.append((i >> j) & 1)
        filled = fill_holes(combo,hl,current_combination)
        if comb_matches(filled,rl):
            matches+=1
    return matches
# m="?###???????? 3,2,1"
# cm=m.split(" ")
# m=cm[0]
# rl=cm[1].split(",")
# rn=[]
# for i in rl:
#     rn.append(int(i))
# rl=rn


def solve(cm):
    t=0
    for j in range(len(cm)):
        m=cm[j][0]
        rl=cm[j][1]
        print(m,"\n",rl)
        tc=get_combos(m,rl)
        t+=tc
        print("count  ",tc)        
    print("total count",t)


            # print(i)
            # for i in fh:
                # print(i)

m=parse()
solve(m)


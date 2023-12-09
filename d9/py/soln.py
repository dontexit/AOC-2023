def parse():
    f = open("inp.txt","r")
    m=[]
    for line in f.readlines():
        line = line.strip().split(" ")
        il=[]
        for c in line:
            try:
                c=int(c)
                il.append(c)

            except:
                continue
        m.append(il)
    return m

# nl=[[0,3,6,9,12,15]]
def cal_exp(num_hist):
    next=0
    for i,nums in enumerate(num_hist):
        diffs=[nums]
        count=0
        while True:
            c=diffs[count]
            z=False
            print("count:",count,"current: ",c)
            for k in range(len(c)):
                    curr=c[k]
                    if curr == 0:
                        z=True
                        continue
                    else:
                        z=False
                        break
            if z == True:
                # print("do reverse",len(diffs))
                ld=len(diffs)
                for r in range(ld-1,-1,-1):
                    # print(r)
                    if r == ld-1:
                        diffs[r].append(0)
                    else:
                        c=diffs[r]
                        p=diffs[r+1]
                        diffs[r].append(c[len(c)-1]+p[len(p)-1])
                next+=diffs[0][len(diffs[0])-1]
                print(diffs)
                break
            el=[]
            for j in range(len(c)-1):
                s=c[j+1]
                f=c[j]
                # print("sec: ",s,"first: ",f)
                nv=s-f
                el.append(nv)
            diffs.append(el)
            count+=1
            print(diffs)
        print(next)
cal_exp(parse())



def parse():
  f=open("inp.txt","r")
  lines=f.readlines()
  m=[]
  for line in lines:
    line=line.strip()
    l=[]
    if line:
      for i in line:
        l.append(i)
      m.append(l)
    # continue
  f.close()
  return m

def tilt_count(m):
  cl=[]
  for i in range(len(m[0])):
    count=len(m)
    ccl=[]
    ccl.append([])
    ts=0
    for j in range(len(m)):
        ce=m[j][i]
        ac=0
        #print(m[j][i])
        # print("current item",ce,type(ce),len(ce))
        if m[j][i] == ".":
            # print("dot dot")
            count-=1
            continue
        if ce == "#":
            # print("has tag #")
            count-=1
            ts+=1

        if m[j][i]=="O":
          # print("inside 0 condition")
          if j==0:
            ccl[0].append(count)
            count-=1
            continue
          
          
          for k in range(j-1,-1,-1):
            c=m[k][i]
            # print("k,i",k,i,c)
            if c =="O" or  c == "#":
                if ac > 0:
                    # print("swapped",m[k+1][i],m[j][i])
                    m[k+1][i]="O"
                    m[j][i]="."
                break
            if k==0 and c==".":
                if k == 0 and c==".":
                        ac+=1
                        m[k][i]="O"
                        m[j][i]="."
                        break
            else:
                ac+=1
          
          ccl[0].append(count+ac)
          count-=1
          continue
                
    ccl.append(ts)
    ct=0
    for celm in ccl[0]:
        ct+=celm-ts
    ts=0
    cl.append(ccl)
    
  # for p in m:
  #       print(p)
  return cl
m=parse()
cl=tilt_count(m)
t=0
for i in cl:
    il=i[0]
    for it in il:
        t+=it
        print(it)
print(t)

        # t+=x
# print(t)

        
# print(t)



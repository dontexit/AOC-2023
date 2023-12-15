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
    # print(l)
    m.append(l)
  f.close()
  return m



def tilt_count(m):
  cl=[]
  for i in range(len(m[0])):
    count=len(m)
    hb=False
    zb=False
    ls=[]
    for j in range(len(m)-8):
        cd={}
        ce=m[j][i]
        ac=0
        #print(m[j][i])
        # print("current item",ce,type(ce),len(ce))
        if m[j][i] == ".":
            # print("dot dot")
            count-=1
            continue
        if ce == "#":
            if zb:
               print("been a zefore before") 
               hb=True
               for e in ls:
                   e["hash_count"]+=1
            count-=1


        if m[j][i]=="O":
          print("inside 0 condition")
          if j==0:
            zb=True
            cd["nums"]=[count]
            cd["hash_count"]=0
            ls.append(cd)
            count-=1
            continue
          
          for k in range(j-1,-1,-1):
            c=m[k][i]
            print("k,i",k,i,c)
            if c =="O" or  c == "#":
                if ac > 0:
                    print("swapped",m[k+1][i],m[j][i])
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
          if not zb or hb:
            hb=False  
            zb=True
            cd["nums"]=[count]
            cd["hash_count"]=0
            ls.append(cd)
            
          else:
            ls[len(ls)-1]["nums"].append(count+ac)

          count-=1
          continue
    cl.append(ls)
  # print(cl)
  return cl
m=parse()
tc=tilt_count(m)
t=0
for i in tc:
    for j in i:
        print(j)
        # for n in j["nums"]:
        #     cc=n-j["hash_count"]
        #     t+=cc
print(t)

        # t+=j["hash_count"]
  # print(i)



      
    

 

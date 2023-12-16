def parse():
  f = open("i1.txt", "r")
  ml = []
  m = []
  lines = f.readlines()
  for id, line in enumerate(lines):
    sl = []
    line = line.strip()
    if line:
      for i in line:
        sl.append(i)
      m.append(sl)
    if not line or id == len(lines) - 1:
      if len(m) > 0:
        ml.append(m)
        m = []

  f.close()
  return ml


def solve_pattern(m):
    ml = len(m)
    rc = [0, 0]
    for i in range(ml):
        # print("first loop",i)
        eq = False
        cj = 0
        for j in range(len(m[0])):
            cj+=1
            if i + 1 < len(m):
                if m[i][j] == m[i + 1][j]:
                    eq = True
                else:
                    eq = False
                    break
        if eq:
            pl=i-1
            for l in range(i+2,ml):
                # print("going back and fourth",l,pl)
                for n in range(len(m[0])):
                    if pl >= 0:
                        cce=m[l][n]
                        ccp=m[pl][n]
                        # print("comparing",cce,ccp,l,n," ",pl,n)
                        if cce == ccp:
                            eq = True 
                        else:
                            eq=False
                            break
                    else:
                        break
                pl-=1
            if eq:
                # print("chad reflection")
                rc[0] = i+1
                # return rc 
            else:
                break
        
    for i in range(len(m[0])):
        eq = False
        for j in range(ml):
            if i + 1 < len(m[0]):
                if m[j][i] == m[j][i + 1]:
                    eq = True
                else:
                    eq = False
                    break
        if eq:
            pl=i-1
            for l in range(i+2,len(m[0])):
                # print("going back and fourth",l,pl)
                for n in range(ml):
                    if pl >= 0:
                        cce=m[n][l]
                        ccp=m[n][pl]
                        # print("comparing",cce,ccp,l,n," ",pl,n)
                        if cce == ccp:
                            eq = True 
                        else:
                            eq=False
                            break
                    else:
                        break
                pl-=1
            if eq:
                # print("chad reflection vert",)
                rc[1] = i+1
                # return rc
            else:
                break

    return rc
mm = parse()
total = 0
# print(mm, len(mm))
c=[0,0]

for l in mm:
    t=solve_pattern(l)  
    c[0]+=t[0]
    c[1]+=t[1]
print(c,c[0]*100+c[1])
  # pass


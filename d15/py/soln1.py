def parse():
  f=open("inp.txt","r")
  lines=f.readlines()
  m=[]
  for line in lines:
    line=line.strip()
    if line:
      line= line.split(",")
      for i in line:
        #print(i)
        m.append(i)
  f.close()
  return m
hashed={}

def hash_symbols(s):
  h=0
  if s in hashed.keys():
    return hashed[s]
  for i in s:
    iv=(h+ord(i))*17
    h=round(iv%256)
    #print(iv,h)
  hashed[s]=h
  return h


def add_box(m):
    box = {}
    for i in m:
        print(i)
        # i=list(i)
        for id,c in enumerate(i):
            # print(c)
            if c == "=" or c=="-":
                label=i[:id]
                h=hash_symbols(label)
                symbol=c
                if symbol == "=":
                    fl = i[id+1:]
                    lens = label + " " + fl
                    if h in box.keys():
                        lenses=box[h]
                        le=False
                        li=0
                        for id,l in enumerate(lenses):
                            if l.split(" ")[0] == label:
                                le=True
                                li=id
                        if le:
                            lenses[li]=lens
                        else:    
                            lenses.append(lens)
                
                    else:
                       box[h]=[lens] 
                else:
                    if h in box.keys():
                        lenses = box[h]
                        for id,l in enumerate(lenses):
                            l = l.split(" ")[0]
                            if l == label:
                                for num in range(id,len(lenses)):
                                    if num == len(lenses)-1:
                                        lenses.pop()
                                    else:
                                        lenses[num]=lenses[num+1]
    
        # print("box",box)        
    return box
  
def calc_focus(boxes):
    t=0
    for k in boxes.keys():
        for id,lens in enumerate(boxes[k]):
            t+= (int(k)+1) *(id+1)*int(lens.split(" ")[1])
    print(t)
 
m=parse()
b=add_box(m)
c=calc_focus(b)

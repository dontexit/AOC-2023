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
    h=iv%256
    #print(iv,h)
  hashed[s]=h
  return h
box = {}
h1=hash("qp")
box[h1]="1"
print(box)




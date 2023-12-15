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
def hash(s):
  h=0
  if s in hashed.keys():
    return hashed[s]
  for i in s:
    iv=(h+ord(i))*17
    h=iv%256
    #print(iv,h)
  hashed[s]=h
  return h

m=parse()
t=0
for s in m:
  t=t+hash(s)
print(t)

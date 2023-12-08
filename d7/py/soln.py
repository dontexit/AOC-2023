def parse_file():
    m=[]
    f=open("input.txt","r")
    lines = f.readlines()
    for line in lines:
        l = line.strip("\n")
        m.append(l)
        print(l)
    f.close()
    return m

value_map={"T":10,
  "J":11,
  "Q":12,
  "K":13,
  "A":14}
#n=[]
#for i in x:
#  s=i.split(" ")
#  l=[]
#  l.append(s[0])  
#  l.append(s[1])
#  n.append(l)
class Hand:
  def __init__(self,hand):
       h=hand.split(" ")
       self.cards=h[0]
       self.bid=h[1]
       self.repeats={}
       self.get_repeats()
       self.order_repeats()
       self.highest=self.repeats[list(self.repeats.keys())[0]]
       
       
  def get_repeats(self):
    
    for card in self.cards:
      if card in self.repeats.keys():
        self.repeats[card]+=1
      else:
        self.repeats[card]=1
  
         
  def order_repeats(self):
    r= (sorted(self.repeats.items(), key=lambda 
                                      t: t[1],reverse=True))
    d={}
    for i in r:
      d[i[0]]=i[1]
    #print('dd',d)
    self.repeats=d

  def __str__(self):
      return "cards: " + self.cards + " highest: "+str(self.highest) +"repeats: "+ str(self.repeats) 
                         
def get_value(card) -> int:
     try:
       a=int(card)
       return a
     except:
       for key in value_map.keys():
         if key==card:
           return value_map[key]       
       return 0

def create_hands_list(hands:list[Hand]):
    hl=[]
    for hand in hands:
        nh=Hand(hand)
        hl.append(nh)
    return hl

def order_highest(hands:list[Hand])->list[int]:
    hl=[]
    for hand in hands:
        hl.append(hand.highest)
    hl.sort(reverse=True)
    return hl
def sort_highest(gl:list[int],hands:list[Hand])->list[Hand]:
    nl=[]
    for i in gl:
        for hand in hands:
            if hand.highest == i:
                    nl.append(hand)
                    hands.remove(hand)
    return nl
def calculate_sort(oh:list[Hand]) -> list[Hand]:
    rl :list[Hand] = []
    for i in range(len(oh)):
        # print("\n",oh[i].repeats,"\n")
        for j in range(i+1,len(oh)-1):
            print(i,j,"\n")
            # print(oh[j+1].repeats)
            k1=list(oh[i].repeats.keys())
            k2=list(oh[j].repeats.keys())
            r1=oh[i].repeats
            r2=oh[j].repeats
            res=False
            for k in range(len(k1)):
                c1 = r1[k1[k]]
                if k <= len(k2)-1:
                    c2=r2[k2[k]]
                else:
                    rl.append(oh[i])
                    res=True
                    break
                
                if c1 > c2:
                    rl.append(oh[i]) 
                    res=True
                    break
                if c1 ==1 and c2==1:
                    break
                if c1 == c2:
                    continue
                if c2 > c1:
                    t=oh[i]
                    oh[i]=oh[j]
                    oh[j]=t
                    rl.append(oh[i])
                    res =True
                    break
            if not res:
                for k in range(len(k1)):
                    c1 =  get_value(k1[k])
                    c2=get_value(k2[k])
                    if c1> c2:
                        rl.append(oh[i]) 
                        res=True
                        break
                    if c1 ==1 and c2==1:
                        break
                    if c1 == c2:
                        continue
                    else:
                        t=oh[i]
                        oh[i]=oh[j]
                        oh[j]=t
                        res=True
                        rl.append(oh[i])
                        break
            else:
                break

    
    return rl

m=parse_file()
hl: list[Hand]=create_hands_list(m)
oh=sort_highest(order_highest(hl),hl)

oh=calculate_sort(oh)

for i in oh:
    print(i.repeats,"\n")


    


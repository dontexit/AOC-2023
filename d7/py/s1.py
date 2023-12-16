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
       self.sort_repeats_values()
       self.highest=self.repeats[list(self.repeats.keys())[0]]
       
       
  def get_repeats(self):
    
    for card in self.cards:
      if card in self.repeats.keys():
        self.repeats[card]+=1
      else:
        self.repeats[card]=1
 
  def sort_repeats_values(self):  
      keys=list(self.repeats.keys())
      repeats = self.repeats
      for i in range(len(keys)-1):
          if self.repeats[keys[i+1]] == self.repeats[keys[i]]:
            if get_value(keys[i+1]) > get_value(keys[i]):
                    t=self.repeats[keys[i]]
                    self.repeats[keys[i]]=self.repeats[keys[i+1]]
                    repeats[keys[i+1]]=t
                
         
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


m=parse_file()
hl: list[Hand]=create_hands_list(m)
oh=sort_highest(order_highest(hl),hl)

# oh=calculate_sort(oh)

for i in oh:
    print(i.repeats,"\n")


    


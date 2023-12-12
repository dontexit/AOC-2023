def parse():
    pass

def get_m(n):
    for i in range(n**2):
        print(i)

m1="""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
ms="""#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
"""
m="#.#.### 1,1,3"

cm=m.split(" ")
m=cm[0]
rl=cm[1]

def comb_matches(m,cl):
    hl=[]
    start=False
    count=0
    # tf={}
    ac=0
    matched=False
    for i in range(len(m)):
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
                    ac+=1
                    if hl[ac] != cl[ac]:
                        matched=False
                        break
                    count=0
        if matched:
            return True
        return False

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
    for i in range(hp):
        m[i]=tf[i]
        
            
def get_matches(m):
    for i in range(len(m)**2):
       print(i,) 
    print("\n")

get_matches([1])
get_matches([2,2])
get_matches([3,3,3])

        
        

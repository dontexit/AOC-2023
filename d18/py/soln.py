

def mark_stem(m, current, start,stop):
    for i in range(start,stop+1):
        m[current[1]][i]="x"
    return m

def build(instrs):
    m=["x"]
    current = [0,0]
    for inst in instrs:
        if inst.direction == "up":
            if  len(m) > inst.step + current[1]:
                m[inst.step + current[1]] = "x" 
            m.append("x")
        elif inst == "down":
            m.append("x")
        elif inst == "left":
            m.append("x")
        elif inst == "right":
            m.append("x")

def go():
    m = [['x'], ['x'], ['x'], ['x'], ['x'], ['x']]
    print(m)
    steps = 5
    dir = "up"
    curr=[4,0]
    lm=len(m)
    start = curr[0]
    end = start - steps

    print("len: ",lm,"steps:",steps,"start: ",start,"end: ",end)
    if end >= 0:
        print("on mark")
        m = mark_up(m,curr,start,end)
    else:
        print("on append")
        m = append_up(m,curr,overflow,step)
    print(m)
        
        
def mark_up(m,current,start,end):
    
    for i in range(start-1,end-1,-1):
        print(i,current[1])
        m[i][current[1]]="+"
        # if i == 0:
            # current[0]=i
    return m
def append_up(m,current,overflow,steps):
    n=[]
    for i in range(steps):
        n.append(["+"])
    for i in range(len(m)):
        n.append(m[i])
    current[0]=0
    m=n
    return m

append_right(m,current,overflow,steps):
    n = []
    for i in range(:)




 

        
go()
        

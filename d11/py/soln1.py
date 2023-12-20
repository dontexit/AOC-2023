from typing import TypedDict
from math import sqrt
class Cordinate(TypedDict):
    x:int
    y:int


class Galaxy(TypedDict):
    name:int  
    position:Cordinate
def parse() -> list[list[str]]:
    m=[]
    f = open("inp.txt","r")
   
    for line in f.readlines():
        nl=[]
        line = line.strip()
        if line:
            for c in line:
                nl.append(c)
            m.append(nl)

    # print(m)
    return m
   
def empty_colmns(m):
    ec=[]
    for i in range(len(m[0])):
        has_star=False
        for j in range(len(m)):
            # print(j,i)
            ci=m[j][i]
            # print(ci)
            if ci == "#":
                has_star=True
        if not has_star:
            ec.append(i)

def empty_rows(m):
    er=[]
    for i in range(len(m)):
        has_star=False
        for j in range(len(m[0])):
            # print(i,j)
            el=m[i,j]
            if el == "#":
                has_star=True
        if not has_star:
            er.append(i)


    
def get_star_cordinates(m:list[list[str]],xvl):
    m1=999999
    gm :list[Galaxy]=[]
    count=0
    ymils = 0
    for i in range(len(m)):
        has_stars=False
        for j in range(len(m[i])):
            xmils=0
            for v in xvl:
                if j >= v:
                    xmils+=m1
            ce = m[i][j]
            if ce == "#":
                has_stars = True
                print(i,j,xmils,ymils)
                gc :Cordinate = {"x":j+xmils,"y":i+ymils}
                g:Galaxy = {"name":count,"position":gc} 
                gm.append(g)
                count+=1
        if not has_stars:
            ymils+=m1

    print(count)
    return gm

def flip_col(m):
    cl=[]
    for i in range(len(m[0])):
        c=[]
        for j in range(len(m)):
            # print(j,i)
            ci=m[j][i]
            # print(ci)
            c.append(ci)
        # print(cl)
        cl.append(c)
    return cl
   
def calculate_distance(c1,c):
    x = c1["x"] - c["x"]
    y = c1["y"] - c["y"]
    return abs(x)+abs(y)
def get_x_voids(m):
    vl=[]
    for i in range(len(m[0])):
        has_stars = False
        for j in range(len(m)):
            # print(j,i)
            cl=m[j][i]
            if cl == "#":
                has_stars = True
        if not has_stars:
            vl.append(i)
    return vl
            

def get_cordinates_sum(m:list[Galaxy]):
    total = 0
    count=0
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            count+=1
            f=m[i]["position"]
            s=m[j]["position"]
            sum=calculate_distance(s,f)
            # print(sum)
            total+=sum
    print(count,total)
    return total
m=parse()
vl=get_x_voids(m)
m= get_cordinates_sum(get_star_cordinates(parse(),vl))



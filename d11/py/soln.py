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
def expand_column(m):
    cl=[]
    for i in range(len(m[0])):
        c=[]
        has_star=False
        for j in range(len(m)):
            # print(j,i)
            ci=m[j][i]
            # print(ci)
            if ci == "#":
                has_star = True
            c.append(ci)
        if not has_star:
             # print("nostar",c)
             for i in range(999999-1):
                cl.append(c)
        else:
             # print("star",c)
             cl.append(c)

    
    return flip_col(cl)
        
def expand_row(m):
    cl=[]
    print("row")
    for i in range(len(m)):
            c=[]
            has_star=False
            for j in range(len(m[0])):
                # print(j,i)
                ci=m[i][j]
                if ci == "#":
                    has_star = True
                c.append(ci)
            if not has_star:
                 # print("nostar",c)
                for i in range(999999-1):
                    cl.append(c)

            else:
                 # print("star",c)
                 cl.append(c)
            
    return cl    
    
    
def get_star_cordinates(m:list[list[str]]):
    gm :list[Galaxy]=[]
    count=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            ce = m[i][j]
            if ce == "#":
                gc :Cordinate = {"x":j,"y":i}
                g:Galaxy = {"name":count,"position":gc} 
                gm.append(g)
                count+=1

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

# def get_columns(m):
#
#     columns = ['' for _ in range(num_columns)]
#
#     # Iterate through each row and append characters to the corresponding column
#     for row in pattern:
#         for col_index, char in enumerate(row):
#             columns[col_index] += char
def calculate_distance(c1,c):
    x = c1["x"] - c["x"]
    y = c1["y"] - c["y"]
    return abs(x)+abs(y)
def get_cordinates_sum(m:list[Galaxy]):
    total = 0
    count=0
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            count+=1
            f=m[i]["position"]
            s=m[j]["position"]
            sum=calculate_distance(s,f)
            print(sum)
            total+=sum
    print(count,total)
    return total
m=parse()           
print(m)
em=expand_column(m)
em=expand_row(em)
em = get_star_cordinates(em)
print(em)
cs=get_cordinates_sum(em)
print(cs)

from typing import TypedDict

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
        for c in line:
            nl.append(c)
        m.append(nl)

    # print(m)
    return m
def expand_column(m):
    cl=[]
    # print(m)
    for i in range(len(m[0])):
        c=[]
        has_star=False
        for j in range(len(m)):
            # print(j,i)
            ci=m[j][i]
            if ci == "#":
                has_star = True
            c.append(ci)
        if not has_star:
             print("nostar",c)
             cl.append(c)
             cl.append(c)
        else:
             print("star",c)
             cl.append(c)
        
    return cl    
        
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
                 print("nostar",c)
                 cl.append(c)
                 cl.append(c)
            else:
                 print("star",c)
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

    # print(gm)
    return gm

def flip_col(m):
    cl=[]
    for i in range(len(m[0])):
        c=[]
        for j in range(len(m)):
                ci=m[j][i]
                c.append(ci)
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
    return x+y
def get_cordinates_sum(m:list[Galaxy]):
    total = 0
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            f=m[i]["position"]
            s=m[j]["position"]
            sum=calculate_distance(s,f)
            total+=sum
    print(total)
m=parse()           

em=expand_column(m)
er=expand_row(em)
get_cordinates_sum(get_star_cordinates(er))
# for i in em:
#     print(i)
# em=flip_col(em)
# for i in em:
#     print(i)
#


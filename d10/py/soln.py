from typing import TypedDict

class Cordinate(TypedDict):
    x:int
    y:int

# inp = """
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# """
    
u:Cordinate={"x":0,"y":1}
d:Cordinate={"x":0,"y":-1}
r:Cordinate={"x":1,"y":0}
l:Cordinate={"x":-1,"y":0}

moves=[u,d,r,l]



def cord_num(cord:Cordinate)->str:
    a:str=str(cord['x']) 
    b:str=str(cord["y"])     
    return a+b
    


pipes={
        "|":{
            "open":[u,d],
            "symbols":{
                cord_num(u):["|","F","7",],
                cord_num(d):["L",]
                },
             },
        "-":{"open":[l,r],
             "symbols":{cord_num(l):["-"],
                        cord_num(r):["L","F","-",]}
             },
        "L":{"open":[u,l],
             "symbols":
             {
                cord_num(u):["|","7","F"],
                cord_num(l):["J","-"],    
                 },
             "close":{
            cord_num(u):r,
            cord_num(l):d
            }},
        "J":{"open":[r,u],
             "symbols":{
                 cord_num(r):["-","L","F"],
                    cord_num(u):["F","|"]},
             "close":{
                cord_num(r):d,
                cord_num(u):l,
            }},
             "7":{"open":[r,d],
            "symbols":{
                cord_num(r):["L","-","F"],
                  cord_num(d):["L","|","J"],
                    },
             "close":{
                cord_num(r):u,
                cord_num(d):l
                 }},
             "F":{"open":[l,d],
                  "symbols":{
                    cord_num(l):["J","7","-"],
                    cord_num(d):["|","L","J"]},
                    "close":{
                        cord_num(l):u,
                        cord_num(d):r,
                    }
                  },
                ".":{},
        # "S":[l,r,u,d],
      }






def parse():
    f = open("inp.txt","r")
    map=[]
    for line in f.readlines():
        line=line.strip()
        l=[]
        for i in line:
            l.append(i)
        map.append(l)

    # print(map)
    return map

def next_pipe_move(move:Cordinate,symbol:str,pipe)->Cordinate|None:
    print("prev_symbol",symbol)
    keys=pipe.keys()
    if "open" in keys:
        next_move=find_cordinate(move,pipe["open"])
        if next_move:
            if "symbols" in keys:
                if symbol in pipe["symbols"][cord_num(next_move)] or  symbol == "S":
                    if "close" in keys:
                        next_move = pipe["close"][cord_num(next_move)]
                        return next_move
                
                    return next_move

def get_pipe_key(c:Cordinate,map:list[list[str]]) -> str|None:
    try:
        pipe = map[c["y"]][c["x"]]
        return pipe
    except:
        pass

def find_cordinate(cordinate,cordinates:list[Cordinate])->Cordinate | None:
    for c in cordinates:
        if c["x"] == cordinate["x"] and c["y"] == cordinate["y"]:
            return c

def check_equal(c:Cordinate,c1:Cordinate)->bool:
    if c["x"] == c1["x"] and c["y"] == c1["y"]:
            return True
    return False

def add(c:Cordinate,c1:Cordinate) -> Cordinate:
    x = c["x"] + c1["x"] 
    y=c["y"] + c1["y"]
    n:Cordinate={"x":x,"y":y}
    return n

def calculate(map):
    for i in range(len(map)):
      for j in range(len(map[i])):
        if map[i][j] == "S":
          cord:Cordinate={"y":i,"x":j}
          print("Start",cord,i,j,map[i][j])
          counts=[]
          for mv in range(len(moves)):
            # print("move",mv)
            counts.append(0)
            cc=cord
            nm=moves[mv]
            # print("from moves arr",nm)
            while True:
                nc=add(cc,nm)
                print("current cordinate",cc,"next move: ",nm,"next cordinate: ",nc)
                pipe_key=get_pipe_key(nc,map)
                prev_key=get_pipe_key(cc,map)
                # print("pipe key",pipe_key)
                if pipe_key and pipe_key !="S":
                    pipe = pipes[pipe_key]
                    # print("pipe: ",pipe)
                    if "open" in pipe.keys():
                        pipes_opens=pipe["open"]
                        print(" pipe: ",pipe_key,"pipe supports: ",pipes_opens,"\n next position",nc," next move",nm,"\n")            
                        print(counts)            
                        # check if the postition we're moving to is valid
                        nm = next_pipe_move(nm,prev_key,pipe)
                        if nm:
                            counts[mv]+=1

                            cc=nc
                            print("has an opening")
                        else:
                            break
                    else:
                        break
                else:
                    break

          print(counts)
                       
          
calculate(parse())        

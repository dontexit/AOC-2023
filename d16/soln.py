import copy


def parse():
    f = open("i.txt","r")
    lines = f.readlines()
    m=[]
    for line in lines:
        l=line.strip()
        ml=[]
        if l:
            for c in l:
                if c == "/":
                    c = "r"
                if c == "\\":
                    c="l"
                # print(c)
                ml.append(c)
                continue
        m.append(ml)
    f.close()    
    return m

parse()

class Cordinate:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def add(self,other):
        return Cordinate(x=self.x+other.x,y=self.y+other.y)

    def __eq__(self, other):
        if isinstance(other, Cordinate):
            if self.x == other.x and self.y == other.y:
                return True
        return False
    def get_dict(self):
        return {"x":self.x,"y":self.y}

    def __str__(self):
        return "x: "+str(self.x)+" y: "+str(self.y)
    def __repr__(self):
        return "x: "+str(self.x)+" y: "+str(self.y)
    
class Top(Cordinate):
    def __init__(self):
        super().__init__(x=0,y=-1)
        self.name="top"
        self.symbol="^"
    def __str__(self):
        return "top " + "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):
        return super().__str__()
class Bottom(Cordinate):
    def __init__(self):
        super().__init__(x=0,y=1)
        self.name="bottom"
        self.symbol="v"
    def __str__(self):
        return "bottom " + "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):    
        return super().__str__()
    
class Left(Cordinate):
    def __init__(self):
        super().__init__(x=-1,y=0)
        self.name="left"
        self.symbol="<"
    def __str__(self):
        return "left " + "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):
        return super().__str__()
class Right(Cordinate):
    def __init__(self):
        super().__init__(x=1,y=0)
        self.name="right"
        self.symbol=">"
    def __str__(self):
        return "right " +  "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):
        return super().__str__()


class Symbol():
    directions = [Right,Left,Top,Bottom]
    def __init__(self,symbol,openings,exits):
        self.symbol=symbol
        self.openings=openings
        self.exits = exits 
    
    def supports(self,direction):
        direction_type = direction
        for opening in self.openings:
            opening = opening()
            if opening.x == direction.x and opening.y == direction.y:
                print("supported")
                return True        
        return False

    def get_exit(self,direction):
        if self.supports(direction):
            print("direction for self",self,direction.name)
            return self.exits[direction.name]
        return []
            
class Pipe(Symbol):
    def __init__(self):
        openings = [Right,Left,Top,Bottom]
        exits = {"right":[Right],"left":[Left],"top":[Left,Right],"bottom":[Left,Right]}
        super().__init__(symbol="-",openings=openings,exits=exits)      
class DownPipe(Symbol):
    def __init__(self):
        openings = [Top,Bottom,Left,Right]
        exits = {"right":[Top,Bottom],"left":[Top,Bottom],"top":[Top],"bottom":[Bottom]}
        super().__init__(symbol="|",openings=openings,exits=exits)
class RightTiltedPipe(Symbol):
    def __init__(self):
        openings = [Top,Left,Right,Bottom]
        exits = {"right":[Top],"left":[Bottom],"top":[Right],"bottom":[Left]}
        super().__init__(symbol="r",openings=openings,exits=exits)
class LeftTiltedPipe(Symbol):
    def __init__(self):
        openings = [Left,Right,Top,Bottom]
        exits = {"right":[Bottom],"left":[Top],"top":[Left],"bottom":[Right]}
        super().__init__(symbol="l",openings=openings,exits=exits)

class CordinateCount(Cordinate):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.count=1



def add_went(went,cord):
    for wentp in went:
        print(wentp.__dict__)
        if wentp.x == cord.x and wentp.y == cord.y:
            wentp.count+=1
            return wentp.count
    new = CordinateCount(cord.x,cord.y) 
    went.append(new)
    return 1


def move(m):
    went = copy.deepcopy(m)
    # left = Left()
    # right = Right()
    # top = Top()
    # bottom = Bottom()
    touched= []
    pipe=Pipe()
    down_pipe=DownPipe()
    right_tilted_pipe=RightTiltedPipe()
    left_tilted_pipe=LeftTiltedPipe()
    symbols=[pipe,down_pipe,right_tilted_pipe,left_tilted_pipe]
    start :Cordinate = Cordinate(x=0,y=0)
    directions=[]
    count = 1000000 
    first = True

    while True:
        count-=1
        if count == 0:
            break
        print("directions",directions)
        if first:
            directions.append([start,Right])
            first = False
        if len(directions) == 0 :
                # print(went)
                for i in went:
                    print(i)
                print(touched)
                print("no more directions")
                break
        else:
            curr_direction = directions[len(directions)-1][1]()
            curr_position =  directions[len(directions)-1][0]

            print("curr_position",curr_position,"curr_direction",curr_direction) 

            if curr_position.x < len(m[0]) and curr_position.x >=0 and curr_position.y < len(m) and curr_position.y >=0 :
                went_count = add_went(touched,curr_position)
                if went_count > 10:
                    directions = []
                    continue 
                # post = copy.deepcopy(curr_position)

                pos = curr_position.get_dict()
                went[pos["y"]][pos["x"]] = "x"
 
                cur_symbol = m[curr_position.y][curr_position.x]
                if cur_symbol == ".":
                    print("on a dot \n",)
                                        
                    # pos = curr_position.get_dict()
                    # went_sym = went[pos["y"]][pos["x"]] 
                    # alr = False
                    # for dirs in [Left,Right,Top,Bottom]:
                    #     if dirs().symbol == went_sym:
                    #         went_sym = "2"
                    #         alr=True
                    #         # break
                    # if not alr:

                    pos = curr_position.get_dict()
                    # went[pos["y"]][pos["x"]] = "#"
                    # for i in went:
                    #     print(i)

                    curr_position=curr_position.add(curr_direction)

                    directions[len(directions)-1][0]=curr_position
                    
                    curr_direction=curr_direction.__class__
                    
                else:
                    symbol_found = False
                    for symbol in [Pipe,DownPipe,RightTiltedPipe,LeftTiltedPipe]:
                        if cur_symbol == symbol().symbol:
                            symbol_found = True
                            print("on symbol",symbol)
                            cur_symbol = symbol()
                            print("check next for", "symbol:",cur_symbol,"direction: ",curr_direction)
                            next =cur_symbol.get_exit(curr_direction)
                            ln=len(next)
                            print("get exits",next,len(next))
                            if ln > 0:
                                    if ln == 2:
                                        # curr_position = copy.deepcopy(curr_position)
                                        directions.pop()
                                        directions.append([curr_position,next[1]])
                                        
                                        curr_position = curr_position.add(next[0]())
                                        directions.append([curr_position,next[0]])
                                        # pos = curr_position.get_dict()
                                        # went[pos["y"]][pos["x"]] = "x"
                                    if len(next) == 1:
                                        directions.pop()
                                        # curr_position = copy.deepcopy(curr_position)
                                        curr_position=curr_position.add(next[0]())
                                        # pos = curr_position.get_dict()
                                        # went[pos["y"]][pos["x"]] = "x"

                                        directions.append([curr_position,next[0]])


                            
                            else:
                                print("not supported")
                                directions.pop()

                    if not symbol_found:
                        print("symbol not found")
                        break

            else:
                print("out of bounds")
                directions.pop()
                if len(directions) > 0:
                    curr_position = curr_position.add(directions[len(directions)-1][1]())
                    directions[len(directions)-1][0]=curr_position
        

m = parse()
move(m)

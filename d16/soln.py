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
    def __str__(self):
        return "top " + "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):
        return super().__str__()
class Bottom(Cordinate):
    def __init__(self):
        super().__init__(x=0,y=1)
        self.name="bottom"
    def __str__(self):
        return "bottom " + "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):    
        return super().__str__()
    
class Left(Cordinate):
    def __init__(self):
        super().__init__(x=-1,y=0)
        self.name="left"
    def __str__(self):
        return "left " + "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):
        return super().__str__()
class Right(Cordinate):
    def __init__(self):
        super().__init__(x=1,y=0)
        self.name="right"
    def __str__(self):
        return "right " +  "x: "+str(self.x)+" y: "+str(self.y)

    def __repr__(self):
        return super().__str__()


class Symbol(Cordinate):
    directions = [Right,Left,Top,Bottom]
    def __init__(self,symbol,openings,exits):
        self.symbol=symbol
        self.openings=openings
        self.exits = exits 
    
    def supports(self,direction):
        direction_type = direction.__class__
        for opening in self.openings:
            if opening == direction_type:
                return True        
        return False

    def get_exit(self,direction):
        if self.supports(direction):
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


def move(m):
    went = copy.deepcopy(m)
    # left = Left()
    # right = Right()
    # top = Top()
    # bottom = Bottom()
    pipe=Pipe()
    down_pipe=DownPipe()
    right_tilted_pipe=RightTiltedPipe()
    left_tilted_pipe=LeftTiltedPipe()
    symbols=[pipe,down_pipe,right_tilted_pipe,left_tilted_pipe]
    start :Cordinate = Cordinate(x=0,y=0)
    directions=[[start,Right]]
    # count = 20
    while True:
        # count-=1
        # if count == 0:
        #     break

        if len(directions) == 0 :
                # print(went)
                for i in went:
                    print(i)
                print("no more directions")
                break
        else:
            curr_direction = directions[len(directions)-1][1]()
            curr_position =  directions[len(directions)-1][0]
            print("curr_position",curr_position,"curr_direction",curr_direction) 

            if curr_position.x < len(m[0]) and curr_position.x >=0 and curr_position.y < len(m) and curr_position.y >=0 :
                # post = copy.deepcopy(curr_position)
                # went[post.x][post.y] = "x"
                cur_symbol = m[curr_position.y][curr_position.x]
                if cur_symbol == ".":
                    print("on a dot")

                    pos = curr_position.get_dict()
                    went[pos["y"]][pos["x"]] = "x"
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
                            next =cur_symbol.get_exit(curr_direction)
                            print("get exits",next)
                            if len(next) > 1:
                                    # curr_position = copy.deepcopy(curr_position)
                                    directions.pop()
                                    directions.append([curr_position,next[1]])
                                    curr_position = curr_position.add(curr_direction)
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
                directions.pop()
        

m = parse()
move(m)

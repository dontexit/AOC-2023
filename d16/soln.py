
from typing import TypedDict


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
                    c = "rt"
                if c == "\\":
                    c="lt"
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
    
class Top(Cordinate):
    def __init__(self):
        super().__init__(x=0,y=-1)
    def __str__(self):
        return "top"
class Bottom(Cordinate):
    def __init__(self):
        super().__init__(x=0,y=1)
    def __str__(self):
        return "bottom"
class Left(Cordinate):
    def __init__(self):
        super().__init__(x=-1,y=0)
    def __str__(self):
        return "left"
class Right(Cordinate):
    def __init__(self):
        super().__init__(x=1,y=0)
    def __str__(self):
        return "right"



class Symbol(Cordinate):
    directions = [Right,Left,Top,Bottom]
    def __init__(self,symbol,openings,exits):
        self.symbol=symbol
        self.openings=openings
        self.exits = exits 
    
    def supports(self,direction):
        for opening in self.openings:
            if opening == direction:
                return True        
        return False

    def get_exit(self,cordinate):
        if self.supports(cordinate):
            return self.exits[str(cordinate)]
            
class Pipe(Symbol):
    def __init__(self):
        openings = [Right,Left,Top,Bottom]
        exits = {"right":[Right],"left":[Left],"top":[Top,Bottom],"bottom":[Top,Bottom]}
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
        super().__init__(symbol="rt",openings=openings,exits=exits)
class LeftTiltedPipe(Symbol):
    def __init__(self):
        openings = [Left,Bottom]
        exits = {"right":[Bottom],"left":[Top],"top":[Left],"bottom":[Right]}
        super().__init__(symbol="lt",openings=openings,exits=exits)


def move(m):
    c1=Cordinate(x=0,y=0)
    c2=Cordinate(x=0,y=0)
    # left = Left()
    # right = Right()
    # top = Top()
    # bottom = Bottom()
    pipe=Pipe()
    down_pipe=DownPipe()
    right_tilted_pipe=RightTiltedPipe()
    left_tilted_pipe=LeftTiltedPipe()
    symbols=[pipe,down_pipe,right_tilted_pipe,left_tilted_pipe]
    directions=[Right]
    while True:
        curr_direction = None

        if len(directions) == 0 and not curr_direction:
                break
        else:
            curr_direction = directions[0]()
            if curr_direction.x < len(m[0]) or curr_direction.x >=0 and curr_direction.y < len(m) and curr_direction.y >=0:
                cur_symbol = m[curr_direction.y][curr_direction.x]
                for symbol in [Pipe,DownPipe,RightTiltedPipe,LeftTiltedPipe]:
                    if cur_symbol == symbol().symbol:
                        cur_symbol = symbol()
                        if cur_symbol.supports(curr_direction):
                            next =cur_symbol.get_exit(curr_direction)
                            if len(next) >0:
                                curr_direction = next[0]
                                directions.append(next[1])
                            else:
                                curr_direction=next[0]


                   
        

m = parse()
move(m)

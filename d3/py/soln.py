
file = open("input.txt","r")
lines = file.readlines()

m = []
for i,line in enumerate(lines):
    l = []
    for j in range(len(line)-1):
        l.append(line[j])
            # curr_pos = [i,j]
            # print(curr_pos[0],curr_pos[1])
            # print(line[j])
    if(len(l)>0):
        m.append(l)
symbols = ["*","#","$",'+']
symbol_pos = []
checked = []
sym_found = []
current_number = []
cn_pos = []
chars = []

exists = {
        'top':0,
        'left':0,
        'bottom':0,
        'right':0
}


def get(cord):
    return m[cord.y][cord.x]

def visited(cord):
    for c in checked:
        if c.x == cord.x and c.y==cord.y:
            return True
    return False


def valid(cord):
    if cord.x < 0 or cord.y < 0 or cord.y > len(m)-1 or cord.x > len(m)[j]-1 :
        return False
    return True

for i in range(len(m)):
    for j in range(len(m[i])):
        if i == 0:
            print("top: \n")
            d = {"x":j,"y":i+1}
            if valid(d):
                print(m[d[]][d.x],'\n')
            

            



        # print(x,y,"\n")
        # print(i," ",j,"\n")
        

    # print(map[x],"\n")

    # print(i,line)

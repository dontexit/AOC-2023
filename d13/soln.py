def parse():
  f = open("i1.txt", "r")
  ml = []
  m = []
  lines = f.readlines()
  for id, line in enumerate(lines):
    sl = []
    line = line.strip()
    if line:
      for i in line:
        sl.append(i)
      m.append(sl)
    if not line or id == len(lines) - 1:
      print()
      if len(m) > 0:
        ml.append(m)
        m = []

  f.close()
  return ml


def solve_pattern(m):
  ml = len(m)
  rc = [0, 0]
  for i in range(ml):
    eq = False
    for j in range(len(m[0])):
      if i + 1 < len(m):
        if m[i][j] == m[i + 1][j]:
          eq = True
        else:
          eq = False
          break
    if eq:
      print("hor")
      rc[0] = (i + 1)

  for i in range(len(m[0])):
    eq = False
    for j in range(ml):
      if i + 1 < len(m[0]):
        if m[j][i] == m[j][i + 1]:
          eq = True
        else:
          eq = False
          break
    if eq:
      print(i + 1, "vert")
      rc[1] = (i + 1)
      break
  if rc[0] > rc[1]:
      return rc[0] 
  else:
    return rc[1]


mm = parse()
total = 0
print(mm, len(mm))
c=0
for l in mm:
  c+= solve_pattern(l)


print(c)
# for p in mm:
#   total+=solve_pattern(mm)
# print(total)


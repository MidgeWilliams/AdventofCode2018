input = open('D3.txt','r').readlines()
part1 = True

claims = []
for line in input:
    claims.append(line.strip())
size = 1000

fabric = []
for i in range (0,size):
    row = []
    for x in range(0,size):
        row.append(0)
    fabric.append(row)

for claim in claims:
    cur = claim.split(' ')
    corner = cur[2].split(',')
    corner[1] = corner[1][0:len(corner[1])-1]
    dim = cur[3].split('x')
    for i in range(0,2):
        corner[i] = int(corner[i])
        dim[i] = int(dim[i])

    for y in range(corner[1],corner[1]+dim[1]):
        for x in range(corner[0],corner[0]+dim[0]):
            if fabric[y][x] == 0:
                fabric[y][x] = 1
            else:
                fabric[y][x] = 2
if not part1:
    for claim in claims:
        cur = claim.split(' ')
        corner = cur[2].split(',')
        corner[1] = corner[1][0:len(corner[1])-1]
        dim = cur[3].split('x')
        for i in range(0,2):
            corner[i] = int(corner[i])
            dim[i] = int(dim[i])

        overlap = False
        for y in range(corner[1],corner[1]+dim[1]):
            for x in range(corner[0],corner[0]+dim[0]):
                if fabric[y][x] == 2:
                    overlap = True
        if overlap == False:
            print cur[0]
else:
    twoClaim = 0
    for line in fabric:
        for inch in line:
            twoClaim += 1 if inch > 1 else 0
    print twoClaim

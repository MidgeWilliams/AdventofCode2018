class FuelBlock:
    def __init__(self, tl, tp, s):
        self.topLeft = tl
        self.totalPower = tp
        self.size = s

    def __eq__(self, o):
        return (self.totalPower == o.totalPower)

    def __ne__(self, o):
        return not (self.totalPower == o.totalPower)

    def __lt__(self, o):
        return (self.totalPower < o.totalPower)

    def __le__(self, o):
        return (self.totalPower <= o.totalPower)

    def __gt__(self, o):
        return (self.totalPower > o.totalPower)

    def __ge__(self, o):
        return (self.totalPower >= o.totalPower)


def getPower(x, y, serial):
    rackID = x + 10
    plvl = rackID * y
    plvl += serial
    plvl *= rackID
    plvl = ((plvl % 1000) - (plvl %100)) / 100
    plvl -= 5
    return plvl

def makeGrid(size, serial):
    grid = []
    for i in range(0,size):
        row = []
        for j in range(0,size):
            row.append(getPower(j+1,i+1,serial))
        grid.append(row)
    return grid

def printGrid(powerGrid):
    for row in powerGrid:
        print row

def sumBlock(grid, x, y, size):
    sum = 0
    for i in range(y,y+size):
        for j in range(x,x+size):
            sum += grid[i][j]
    return sum

def findSquares(powerGrid):
    squares = []
    for size in range(1,30):#Supposed to be up to 300 but figured didn't need to
        for y in range(0,len(powerGrid)-(size-1)):
            for x in range(0, len(powerGrid)-(size-1)):
                tempx = x+1
                tempy = y+1
                topLeft = '%d,%d'%(tempx,tempy)
                totalPower = sumBlock(powerGrid, x, y, size)
                block = FuelBlock(topLeft, totalPower, size)
                squares.append(block)
    return squares

# serial = 18
serial = 1723
size = 300
powerGrid = makeGrid(size, serial)
squareBlocks = findSquares(powerGrid)
squareBlocks.sort()
squareBlocks.reverse()

print '%s,%d'%(squareBlocks[0].topLeft,squareBlocks[0].size)

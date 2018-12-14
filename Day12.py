class Pot:
    def __init__(self, number, plant):
        self.num = number
        self.planter = plant

    def __str__(self):
        return self.planter

class Instruction:
    def __init__(self, pttrn, rslt):
        self.pattern = pttrn
        self.result = rslt

    def __str__(self):
        return self.result

    def __eq__(self, o):
        return self.pattern == o

initial = '#....##.#.#.####..#.######..##.#.########..#...##...##...##.#.#...######.###....#...##..#.#....##.##'
# initial = '#..#.#..##......###...###'

def finalCount(pots):
    count = 0
    for i in range(0,len(pots)):
        if pots[i].hasPlant: count += pots[i].num
    return count

def makePots(initial):
    pots = []
    num = 0
    for pot in initial:
        newPot = Pot(num,pot)
        pots.append(newPot)
        num += 1
    return pots

def processInstr():
    instSet = []
    instr = open('D12.txt','r').readlines()
    for i in range(0,len(instr)):
        instr[i] = instr[i].split('=>')
        instr[i][0] = instr[i][0].strip()
        instr[i][1] = instr[i][1].strip()
        newInst = Instruction(instr[i][0],instr[i][1])
        instSet.append(newInst)
    return instSet

def getFiveAdj(pots,i):
    genSet = ''

    for x in range(i-2,i+3):
        if x < 0 or x > len(pots) - 1:
            genSet += '.'
        else:
            genSet += str(pots[x])

    return genSet

def update(pots, instSet):
    nextGen = []
    for i in range(-1,len(pots)+1):
        genSet = getFiveAdj(pots,i)
        match = instSet.index(genSet)
        plant = instSet[match].result

        if i < 0 or i > len(pots) - 1:
            potNum = 0
            if plant == '#':
                if i < 0:
                    potNum = pots[0].num - 1
                elif i > len(pots) - 1:
                    potNum = pots[len(pots)-1].num + 1

                newPot = Pot(potNum,plant)
                nextGen.append(newPot)
        else:
            potNum = pots[i].num
            newPot = Pot(potNum,plant)
            nextGen.append(newPot)

    return nextGen

def getTotal(pots):
    total = 0
    for pot in pots:
        total += pot.num if pot.planter == '#' else 0
    return total


part2 = True
pots = makePots(initial)
instr = processInstr()
if part2:
    for i in range(0,90):
        pots = update(pots, instr)
    total = getTotal(pots)
    total += (50000000000-90)*15
    print total
    # for i in range(0,150):
    #     pots = update(pots, instr)
    #     cur = getTotal(pots)
    #     print '(Generation %d)Cur: %d \t\t Difference from old: %d' %(i+1,cur, cur-prev)
    #     prev = cur
else:
    for i in range(0,20):
        pots = update(pots, instr)

    print getTotal(pots)

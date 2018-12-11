from Day7Obj import Step
from Day7Obj import Elf

require = open('D7.txt', 'r').readlines()
for i in range(0,len(require)):
    require[i] = require[i].split(' ')



steps = []
for line in require:
    step1 = Step(line[1])
    step2 = Step(line[7])
    if step1 not in steps:
        steps.append(step1)
    if step2 not in steps:
        steps.append(step2)
    ind1 = steps.index(step1)
    ind2 = steps.index(step2)
    steps[ind2].addWaiting(steps[ind1])

steps.sort()

elves = []
for i in range(0,5):
    elves.append(Elf(i))
order = []
time = 0

def claimNew(elf):
    global steps
    i = 0
    while i < len(steps) and not elf.working:
        if (not (steps[i].done)) and (not (steps[i].active)) and steps[i].checkReady():
            steps[i].active = True
            elf.working = True
            elf.curr = steps[i]
        else:
            i += 1

while not (len(order) == len(steps)):
    for elf in elves:
        if elf.working:
            elf.curr.time -= 1
            if elf.curr.time <= 0:
                elf.curr.active = False
                elf.curr.done = True
                order.append(elf.curr)
                elf.working = False
                claimNew(elf)
        else:
            claimNew(elf)
    time += 1
print time -1


# str_order = ''
# for step in order:
#     str_order += step.name
# print str_order

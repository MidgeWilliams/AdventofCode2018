class Step:
    def __init__(self, letter):
        self.name = letter
        self.waiting = []
        self.done = False

    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return str(self.name)

    def __eq__(self, o):
        return (self.name == o.name)

    def __ne__(self, o):
        return not (self.name == o.name)

    def __lt__(self, o):
        return (self.name < o.name)

    def __le__(self, o):
        return (self.name <= o.name)

    def __gt__(self, o):
        return (self.name > o.name)

    def __ge__(self, o):
        return (self.name >= o.name)

    def addWaiting(self, otherStep):
        self.waiting.append(otherStep)

    def checkReady(self):
        ready = True
        for step in self.waiting:
            ready = ready and step.done
        return ready

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
order = []

i = 0
while not (len(order) == len(steps)):
    if (not (steps[i].done)) and steps[i].checkReady():
        order.append(steps[i])
        steps[i].done = True
        i = 0
    else:
        i = (i + 1) % len(steps)

str_order = ''
for step in order:
    str_order += step.name
print str_order

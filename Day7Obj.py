class Step:
    def __init__(self, letter):
        self.name = letter
        self.waiting = []
        self.done = False
        self.active = False
        self.time = abs((ord('A')-ord(self.name))) + 61

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

class Elf:
    def __init__(self, nm):
        self.name = nm
        self.working = False
        self.curr = None

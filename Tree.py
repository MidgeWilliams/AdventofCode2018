class Tree:
    def __init__(self, ind, nmChild, nmMeta):
        self.start = ind
        self.child_count = nmChild
        self.meta_count = nmMeta
        self.children = []
        self.metadata = []

    def __str__(self):
        return str(self.start)

    def __repr__(self):
        return str(self.start)

    def __eq__(self, o):
        return (self.start == o.start)

    def __ne__(self, o):
        return not (self.start == o.start)

    def __lt__(self, o):
        return (self.start < o.start)

    def __le__(self, o):
        return (self.start <= o.start)

    def __gt__(self, o):
        return (self.start > o.start)

    def __ge__(self, o):
        return (self.start >= o.start)

    def sum_meta(self):
        temp = 0
        for i in range(0,len(self.metadata)):
            temp += self.metadata[i]
        return temp

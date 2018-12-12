class PointMine:
    def __init__(self, x_coor, y_coor):
        self.x = x_coor
        self.y = y_coor

    def __str__(self):
        return ('(%d, %d)'% (self.x,self.y))

class Star:
    def __init__(self, pos_initial, velocity):
        self.pos = pos_initial
        self.vel = velocity

    def move(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def __str__(self):
        return ('%s --> %s' % (self.pos, self.vel))

import re
import time
from graphics import *
info = open('D10.txt','r').readlines()
# info = open('test.txt','r').readlines()

def makePointMine(point):
    point = point.split(',')
    point[0] = int(point[0].strip())
    point[1] = int(point[1].strip())
    newPointMine = PointMine(point[0],point[1])
    return newPointMine

def normalize():
    global stars, height, width
    minx = 0
    miny = 0
    for i in range(1, len(stars)):
        if stars[minx].pos.x > stars[i].pos.x:
            minx = i
        if stars[miny].pos.y > stars[i].pos.y:
            miny = i

    offsetx = stars[minx].pos.x
    offsety = stars[miny].pos.y

    for i in range(0, len(stars)):
        stars[i].pos.x -= offsetx
        stars[i].pos.y -= offsety
        if width < stars[i].pos.x:
            width = stars[i].pos.x
        if height < stars[i].pos.y:
            height = stars[i].pos.y

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def printAll():
    global stars
    for star in stars:
        print star.pos.x
    print '\n\n\n'
    for star in stars:
        print star.pos.y
    for i in range(0,10):
        print '\n'

def update():
    global stars
    for star in stars:
        star.move()
    # for star in stars:
    #     pt = Point(star.pos.x, star.pos.y)
    #     pt.draw(win)
    # win.getMouse()
    # clear(win)

stars = []

for i in range(0,len(info)):
    info[i] = re.split('<|>', info[i])
    position = makePointMine(info[i][1])
    velocity = makePointMine(info[i][3])
    cur = Star(position, velocity)
    stars.append(cur)

def getYRange():
    global stars
    min = stars[0].pos.y
    max = stars[0].pos.y
    for i in range(1,len(stars)):
        if min > stars[i].pos.y:
            min = stars[i].pos.y
        if max < stars[i].pos.y:
            max = stars[i].pos.y
    return max-min

curRange = getYRange()
gettingsmaller = True
counter = 0
while gettingsmaller:
    update()
    newRange = getYRange()
    if newRange < curRange:
        counter += 1
        curRange = newRange
    else:
        gettingsmaller = False
printAll()
print counter, ': ',curRange

# normalize()
# print 'Height: %s Width %s'% (height, width)
#
# for i in range(0,50):
#     update()



# while(True):
#     win = GraphWin("Message", width+1, height+1)
#     update(win)
#     print '\n'
#     win.close()

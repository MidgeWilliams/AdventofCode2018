from Point import Point
part1 = False

coord = open('D6.txt','r').readlines()
plot_size = []
for i in range(0,len(coord)):
    coord[i] = coord[i].strip()
    temp = coord[i].split(',')
    temp[0] = temp[0].strip()
    temp[1] = temp[1].strip()
    coord[i] = Point(int(temp[0]),int(temp[1]))
    plot_size.append(0)


def dist(cur, dest):
    dist = 0
    dist += abs(cur.x-dest.x)
    dist += abs(cur.y-dest.y)
    return dist

def get_closest(cur):
    global coord
    min = 0
    for i in range(1,len(coord)):
        if dist(cur,coord[min]) > dist(cur, coord[i]):
            min = i
    for i in range(0,len(coord)):
        if i != min and dist(cur,coord[min]) == dist(cur, coord[i]):
            return -1
    return min

if part1:
    for x in range(0,400):
        for y in range(0,400):
            cur = Point(x,y)
            closest = get_closest(cur)
            #print cur, " closest: ", coord[closest]
            if closest != -1:
                if x == 0 or x == 399 or y == 0 or y == 399:
                    plot_size[closest] = -999
                elif plot_size[closest] != -999:
                    plot_size[closest] += 1

    most_close = 0
    for i in range(1,len(plot_size)):
        if plot_size[most_close] < plot_size[i]:
            most_close = i

    print plot_size[most_close]
else:
    limit = 10000
    passing_points = 0
    for x in range(0,400):
        for y in range(0,400):
            cur = Point(x,y)
            total_dist = 0
            for point in coord:
                total_dist += dist(cur,point)
            if total_dist < limit:
                passing_points += 1
    print passing_points

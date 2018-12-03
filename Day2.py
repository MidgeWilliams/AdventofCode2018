input = open('D2.txt','r').readlines()
boxIds = []
for line in input:
    boxIds.append(line.strip())

part1 = False

#Given the Id string and the number of reps it's looking for (2 or 3)
def checkRep(str, num):
    id = str
    for i in range(0,len(id)):
        let = id[i]
        if let != '_':
            cur = id[i+1:len(id)]
            count = 1
            while let in cur:
                count += 1
                ind = cur.find(let)
                cur = cur[ind+1:len(cur)]
            if count == num:
                return True
            id = id.replace(let,"_")
    return False

def removeChar(str, ind):
    rem = str[0:ind]+str[ind+1:len(str)]
    return rem

if part1:
    doub = 0
    trip = 0

    for id in boxIds:
        doub += 1 if checkRep(id, 2) else 0
        trip += 1 if checkRep(id, 3) else 0

    print doub * trip
else:
    length = len(boxIds[0])
    for i in range(0,length):
        tempIds = []
        for id in boxIds:
            tempIds.append(removeChar(id,i))
        for x in range(0,len(tempIds)):
            cur = tempIds[x]
            for y in range(x+1, len(tempIds)):
                if cur == tempIds[y]:
                    print cur

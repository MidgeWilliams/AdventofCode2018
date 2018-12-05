polymer = open('D5.txt').read()
polymer = polymer.strip()
#polymer = 'dabAcCaCBAcCcaDA'
l2c = 32 #lower to capital is 32 diff

def shrinkPoly(polymer):
    changed = True
    while changed:
        changed = False
        i = 1
        while i < len(polymer):
            ltr1 = polymer[i-1]
            ltr2 = polymer[i]
            if abs(ord(ltr1)-ord(ltr2)) == l2c:
                polymer = polymer[0:i-1] + polymer[i+1:len(polymer)]
                changed = True
            else:
                i += 1
    return polymer

part1 = False
if part1:
    print len(shrinkPoly(polymer))
else:
    lowPoly = polymer.lower()
    letters = []
    for i in range(0,len(lowPoly)):
        if lowPoly[i] not in letters: letters.append(lowPoly[i])

    final_lengths = []
    count = 0
    for letter in letters:
        upper = ord(letter) - l2c
        upper = chr(upper)
        tempPoly = polymer
        tempPoly = tempPoly.replace(letter,'')
        tempPoly = tempPoly.replace(upper,'')
        final_lengths.append(len(shrinkPoly(tempPoly)))
        count += 1
        if count%5 == 0:
            print count, letter
    final_lengths.sort()
    print final_lengths[0]

freqChanges = open('D1.txt', 'r').readlines()
freq = 0

part1 = False

nodouble = True
allFreq = []
allFreq.append(freq)
if part1:
    for change in freqChanges:
        cur = change.strip()
        num = int(cur[0:len(cur)])
        freq += num
else:
    while(nodouble):
        for change in freqChanges:
            cur = change.strip()
            num = int(cur[0:len(cur)])
            freq += num
            if freq in allFreq:
                nodouble = False
                break
            else:
                allFreq.append(freq)

print freq

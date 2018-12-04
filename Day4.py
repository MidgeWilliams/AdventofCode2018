input = open('D4.txt','r').readlines()
shift_log = []
for line in input:
    shift_log.append(line.strip().split(' '))

def next_day(cur):
    today = cur.split('-')
    today[1] = int(today[1])
    today[2] = int(today[2])

    days31 = [5,7,8,10]

    if today[1] in days31 and today[2] == 31:
        today[1] += 1
        today[2] = 1
    elif today[2] == 30:
        today[1] += 1
        today[2] = 1
    else:
        today[2] += 1
    cur_date = str(today[0]) + '-'
    if today[1] / 10 < 1:
        cur_date += '0'
    cur_date += str(today[1]) + '-'
    if today[2] / 10 < 1:
        cur_date += '0'
    cur_date += str(today[2])

    return cur_date

date = []
guard = []
info = []
for i in range(0,len(shift_log)):
    cur_date = shift_log[i][0][1:len(shift_log[i][0])]
    shift_log[i][0] = cur_date
    cur_time = shift_log[i][1][0:len(shift_log[i][1])-1]
    shift_log[i][1] = cur_time

    if cur_time[0:2] > '00':
        cur_date = next_day(cur_date)

    if cur_date not in date:
        date.append(cur_date)
        guard.append([])
        info.append([])

    ind = date.index(cur_date)
    if shift_log[i][2] == 'Guard':
        guard[ind] = shift_log[i][3][1:len(shift_log[i][3])]
    elif shift_log[i][2] == 'falls' or shift_log[i][2] == 'wakes':
        cur_info = [cur_time]
        cur_info.append(shift_log[i][2])
        info[ind].append(cur_info)

# for i in range(0,len(date)):
#     print date[i], " ", guard[i]
#     for entry in info[i]:
#         print "   ", entry

def makeTimes(inf):
    times = []
    for thing in inf:
        cur = thing[0].split(':')
        min = int(cur[1])
        times.append(min)
    times.sort()
    return times


guardNum = []
guardHours = []
for i in range(0,len(date)):
    if guard[i] not in guardNum:
        guardNum.append(int(guard[i]))
        guardHours.append([])
    ind = guardNum.index(int(guard[i]))
    times = makeTimes(info[i])
    x = 0
    while x < len(times):
        for y in range(times[x],times[x+1]):
            guardHours[ind].append(y)
        x += 2

part1 = False
if not part1:
    maxNum = []
    maxCnt = []
    for i in range(0, len(guardNum)):
        hour = []
        count = []
        for time in guardHours[i]:
            if time not in hour:
                hour.append(time)
                count.append(0)
            ind = hour.index(time)
            count[ind] += 1

        modeHour = 0
        for j in range(1,len(hour)):
            if count[j] > count[modeHour]:
                modeHour = j
        hourtoadd = -1
        countoadd = 0
        if len(hour) > 0:
            hourtoadd = hour[modeHour]
            countoadd = count[modeHour]
        maxNum.append(hourtoadd)
        maxCnt.append(countoadd)

    mostCommon = 0
    for i in range(1,len(guardNum)):
        if maxCnt[i] > maxCnt[mostCommon]:
            mostCommon = i

    print guardNum[mostCommon], ' @ ', maxNum[mostCommon], ' = ', guardNum[mostCommon]*maxNum[mostCommon]

else:
    max = 0
    for i in range(1,len(guardHours)):
        if len(guardHours[i]) > len(guardHours[max]):
            max = i

    sleepiest = guardHours[max]
    sleepiest.sort()

    hour = []
    count = []
    for time in sleepiest:
        if time not in hour:
            hour.append(time)
            count.append(0)
        ind = hour.index(time)
        count[ind] += 1

    modeHour = 0
    for i in range(1,len(hour)):
        if count[i] > count[modeHour]:
            modeHour = i
    print guardNum[max] * hour[modeHour]

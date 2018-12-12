class Player:
    def __init__(self, num):
        self.name = num
        self.score = 0

from collections import deque

input = '462 players; last marble is worth 71938 points'  #Actual input
# input = '10 players; last marble is worth 1618 points' # high score is 8317

input = input.split(' ')

players = []
for i in range(0,int(input[0])):
    players.append(Player(i))
last = int(input[6])

part2 = False
if part2:
    last *= 100

last += 1
marbles = deque([0])
turn = 0
for i in range(1, last):
    if i % 23 == 0:
        players[turn].score += i
        marbles.rotate(7)
        players[turn].score += marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(i)
    turn = (turn + 1) % len(players)

# FIRST WAY, NEVER WOULD HAVE FOUND OUT PART 2
# else:
#     last += 1
#     marbles = []
#     marbles.append(0)
#
#     turn = 0
#     cur = 0
#
#     for i in range(1, last):
#         if i % 23 != 0:
#             next_place = (cur + 1) % (len(marbles)) + 1
#             marbles.insert(next_place,i)
#             cur = next_place
#         else:
#             players[turn].score += i
#             seven = (cur + (len(marbles)-7))% len(marbles)
#             players[turn].score += marbles[seven]
#             del marbles[seven]
#             cur = seven
#         turn = (turn + 1) % len(players)

max = 0
for i in range(1, len(players)):
    if players[max].score < players[i].score:
        max = i
print players[max].score

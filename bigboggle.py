cubes = {'B K B J Z X',
'A A F R S A',
'D H O T D N',
'O T T T M E',
'D N A N E N',
'I I E I T T',
'T I L S E P',
'E E E E A A',
'N E M N G A',
'S F R I A A',
'O T T U O O',
'S U S E N S',
'G E E U M A',
'A S I R F Y',
'G R R V O W',
'H Z R L O D',
'L E T I I S',
'A E M E E E',
'W O N O T U',
'H O L D H R',
'C T E S C N',
'P Y I Y S R',
'O W D N H H',
'T I S C E P',
'An He Er In Qu Th'}

from random import random
import math
import time

def pickCubeSide():
    return math.floor(random() * 6)
def splitAndPick(c):
    return c.split()[pickCubeSide()]

class BigBoggle:
    def __init__(self, n=5):
        self.board = [splitAndPick(c) for c in cubes]
        self.n = n
        n_squared = n*n
        if len(self.board) < n_squared:
            cube_copies = list(cubes)
            while len(self.board) < n_squared:
                try:
                    c = cube_copies.pop()
                except:
                    cube_copies = list(cubes)
                    c = cube_copies.pop()
                self.board.append(splitAndPick(c))
        print(self)


    def startGame(self):
        self.time = time.clock()
        elapsed = 0
        print(self)
        print('READY')
        time.sleep(.5)
        print('SET')
        time.sleep(.5)
        print('GO')
        while elapsed <= 180:
            print(math.floor(elapsed))
            time.sleep(10)
            elapsed = time.clock() - self.time
        print(elapsed)
        print('TIME')
        i = 0
        while (i < 10):
            print('\n')
            i += 1

    def __repr__(self):
        nums = [i for i in range(self.n*self.n)]
        rows = nums[0::self.n]
        st = ''
        for i in rows:
            for k in range(i, i+self.n):
                spaces = '  '
                if len(self.board[k]) > 1:
                    spaces = ' '
                st += self.board[k] + spaces
            st += '\n'
        return st

#BB = BigBoggle()
alphabet = 'A B C D E F G H I J K L M N O P Qu R S T U V W X Y Z In He Th Er An'.split()
cubeletters = []
for c in cubes:
    cubeletters.extend(c.split())

freq_dict = dict()
for letter in alphabet:
    freq = 0
    for c in cubeletters:
        if c == letter:
            freq += 1
    freq_dict[letter] = freq
print(freq_dict)

#BB5 = BigBoggle(5)
##BB6 = BigBoggle(6)
#BB7 = BigBoggle(7)
#BB8 = BigBoggle(8)

for i in range(5,12):
    bb = BigBoggle(i)

#bb.startGame()
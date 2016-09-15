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
import tkinter as tk

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
            time.sleep(1)
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

def current_iso8601():
    """Get current date and time in ISO8601"""
    # https://en.wikipedia.org/wiki/ISO_8601
    # https://xkcd.com/1179/
    return time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())

class boggleApp(tk.Canvas):
    def __init__(self, master = None, w = 700, h = 600):
        if master == None:
            master = tk.Tk()
            master.wm_title('Big Boggle')
        super(boggleApp, self).__init__(master, width = w, height = h)
        self.pack()

       # self.bb = BigBoggle(5)
        self.r = self.create_rectangle(25, 25, 500, 500)
        self.insert_board(BigBoggle(5))
        self.initial_time = time.clock()
        self.time_keeper = self.create_text(25, 580, font=("Purisa", 16), text='0:00')
        self.create_restart()
        #mini = tk.Canvas(self.master, width = 50,height = 50)
        self.create_bitmap(80, 580, bitmap = 'hourglass')
        self.after(180000, func = self.fill_yellow)

       # self.restart_timer()
               # self.bind(i, func = self.increment_timer)
       # self.bind(self.time_keeper,)
        #hourglass.scale(1.5, 1.5)
       # self.event_generate(sequence=, )

        #self.after(100, func=self.increment_timer)

    def fill_yellow(self):
        self.itemconfig(self.r, fill = "yellow")

    def insert_board(self, board):
        self.board = board
        letters = (k for k in board.board)

        nums = [i for i in range(575)]
        axes = nums[80::80]
        rg = range(board.n)
        for y in rg:
            for x in rg:
                self.create_text(axes[x], axes[y], font=("Purisa", 30), text=next(letters))

    def create_restart(self):
        self.restart = tk.Button(self.master)
        self.restart["text"] = "Restart"
        self.restart.pack(side="right")
        self.restart["command"] = self.restart_timer


    def while_timer(self):
        elapsed = 0
        delta = 0
        while elapsed < 30000:
            elapsed = time.clock() - self.initial_time
            #print(elapsed)
            #print(delta)
            if elapsed - delta > 1000:
                self.increment_timer(elapsed)
                delta = elapsed



    def increment_timer(self, new_time = None):

        self.elapsed = time.clock() - self.initial_time
        if not new_time == None:
            self.elapsed = '3:00'

        self.itemconfig(self.time_keeper, text=math.floor(self.elapsed))
        self.after(100, self.increment_timer)


    def restart_timer(self):
        self.board.startGame()
       # self.initial_time = 0
        #self.while_timer()
      #  self.event_gen = (self.after(i, self.increment_timer) if i %100 == 0 else 0 for i in range(30000 ))
      # next(self.event_gen)
        #self.itemconfig(self.time_keeper, text='0:00')
       # self.after_idle(self.increment_timer)
      #  self.bind(self.time_keeper, )


bb = boggleApp()
bb.mainloop()




    #w = Canvas(master, width=200, height=100)
    #w.pack()

    #w.create_line(0, 0, 200, 100)
    #w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

    #w.create_rectangle(50, 25, 150, 75, fill="blue")

   # mainloop()

#BB = BigBoggle()
# alphabet = 'A B C D E F G H I J K L M N O P Qu R S T U V W X Y Z In He Th Er An'.split()
# cubeletters = []
# for c in cubes:
#     cubeletters.extend(c.split())
#
# freq_dict = dict()
# for letter in alphabet:
#     freq = 0
#     for c in cubeletters:
#         if c == letter:
#             freq += 1
#     freq_dict[letter] = freq
# print(freq_dict)

#BB5 = BigBoggle(5)
##BB6 = BigBoggle(6)
#BB7 = BigBoggle(7)
#BB8 = BigBoggle(8)

#for i in range(5,12):
 #   bb = BigBoggle(i)


#bb.startGame()


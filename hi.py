def inputIsFalse(a, b, board):
    if a < 0 or a > 2 or b < 0 or b > 2:
        print("Wrong input! Should be either 0, 1, or 2. Pls type again!")
        return True
    elif board.board[b][a] != "-":
        print("That location is already marked. Please pick another one!")
        return True
    else:
        return False

class Board():
	def __init__(self):
		self.winner = "-"
		self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]

	def getData(self):
		print("{0} {1} {2} \n{3} {4} {5} \n{6} {7} {8}".format(
                   self.board[0][0],
                   self.board[0][1],
                   self.board[0][2],
                   self.board[1][0],
                   self.board[1][1],
                   self.board[1][2],
                   self.board[2][0],
                   self.board[2][1],
                   self.board[2][2]
        )) 

class SuperBoard():
    def __init__(self):
        self.boardGrid = [[Board(),Board(),Board()],[Board(),Board(),Board()],[Board(),Board(),Board()]]

    def getData(self):
        print("{0} {1} {2} \n{3} {4} {5} \n{6} {7} {8}".format(
                   self.boardGrid[0][0].getData(),
                   self.boardGrid[0][1].getData(),
                   self.boardGrid[0][2].getData(),
                   self.boardGrid[1][0].getData(),
                   self.boardGrid[1][1].getData(),
                   self.boardGrid[1][2].getData(),
                   self.boardGrid[2][0].getData(),
                   self.boardGrid[2][1].getData(),
                   self.boardGrid[2][2].getData()
        )) 

class Player:
    def __init__(self, name, sign):
           self.name = name
           self.sign = sign

def updateBoard(y, x, boardObj, player):
   boardObj.board[y][x] = player.sign 

# tuples to indicate certain locations
# left upper, left middle, left lower
lu = (0,0) 
lm = (1,0)
ll = (2,0)
# middle upper, middle middle, middle lower
mu = (0,1) 
mm = (1,1)
ml = (2,1)
# right upper, right middle, right lower
ru = (0,2) 
rm = (1,2)
rl = (2,2)

# tuples to indicate groups of tuples that lie in a straight line
# naming: from _ _ to _ _ . ex: from left upper to right lower: lurl
lull = (lu, lm, ll)
muml = (mu, mm, ml)
rurl = (ru, rm, rl)
luru = (lu, mu, ru)
lmrm = (lm, mm, rm)
llrl = (ll, ml, rl)
lurl = (lu, mm, rl)
llru = (ll, mm, ru)

# tuple of winner groups of tuples
winners = (lull, muml, rurl, luru, lmrm, llrl, lurl, llru)

def gb(tup, board):
    return board.board[tup[0]][tup[1]]

def checkWinner(board):
    b = board.board                
    for t in winners:
        if gb(t[0], board) == gb(t[1], board) == gb(t[2], board) != "-":
            return True
    return False

print("Welcome to Boter, Kaas en Eieren. To play, first enter two user names.")
# p1 = Player(input("user 1 (who will play as X): "), "X")
# p2 = Player(input("user 2 (who will play as O): "), "O")
p1 = Player("p1", "X")
p2 = Player("p2", "O")


# Board variables
superBoard = Board()
b1 = Board()
b2 = Board()
b3 = Board()
b4 = Board()
b5 = Board()
b6 = Board()
b7 = Board()
b8 = Board()
b9 = Board()


print("Initial board:")
superBoard.getData()

print("Enter coordinates one by one. First the X, then the Y.")

winner = "-"
finished = False
while (not finished):
    u1x = int(input(p1.name + " X: "))
    u1y = int(input(p1.name + " Y: "))
    while inputIsFalse(u1x, u1y, superBoard):
        u1x = int(input(p1.name + " X: "))
        u1y = int(input(p1.name + " Y: "))
   
    
    updateBoard(u1y, u1x, superBoard, p1)
    if checkWinner(superBoard):
        print(p1.name + " has won!!")
        superBoard.getData()
        break

    superBoard.getData()

    u2x = int(input(p2.name + " X: "))
    u2y = int(input(p2.name + " Y: "))
    while inputIsFalse(u2x, u2y, superBoard):
        u2x = int(input(p2.name + " X: "))
        u2y = int(input(p2.name + " Y: "))

    updateBoard(u2y, u2x, superBoard, p2)
    if checkWinner(superBoard):
        print(p2.name + " has won!!")
        superBoard.getData()
        break
    
    superBoard.getData()


# utility functions


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

    def getRawData(self):
        return "{} {} {}\n{} {} {}\n{} {} {}".format(
            self.board[0][0], self.board[0][1], self.board[0][2], 
            self.board[1][0], self.board[1][1], self.board[1][2],
            self.board[2][0], self.board[2][1], self.board[2][2]
        )

    def getUpperData(self):
        return "{} {} {}".format(self.board[0][0], self.board[0][1], self.board[0][2])
				   
    def getMiddleData(self):
        return "{} {} {}".format(self.board[1][0], self.board[1][1], self.board[1][2])

    def getLowerData(self):
        return "{} {} {}".format(self.board[2][0], self.board[2][1], self.board[2][2])

class SuperBoard():
    def __init__(self):
        self.boardGrid = [[Board(),Board(),Board()],[Board(),Board(),Board()],[Board(),Board(),Board()]]

    def getData(self):
        print(
				"{} | {} | {} \n{} | {} | {} \n{} | {} | {} \n~~~~~~~~~~~~~~~~~~~~~~\n{} | {} | {} \n{} | {} | {} \n{} | {} | {} \n~~~~~~~~~~~~~~~~~~~~~~\n{} | {} | {} \n{} | {} | {} \n{} | {} | {}"
					.format(
                   self.boardGrid[0][0].getUpperData(),
                   self.boardGrid[1][0].getUpperData(),
                   self.boardGrid[2][0].getUpperData(),
                   self.boardGrid[0][0].getMiddleData(),
                   self.boardGrid[1][0].getMiddleData(),
                   self.boardGrid[2][0].getMiddleData(),
                   self.boardGrid[0][0].getLowerData(),
                   self.boardGrid[1][0].getLowerData(),
                   self.boardGrid[2][0].getLowerData(),

                   self.boardGrid[0][1].getUpperData(),
                   self.boardGrid[1][1].getUpperData(),
                   self.boardGrid[2][1].getUpperData(),
                   self.boardGrid[0][1].getMiddleData(),
                   self.boardGrid[1][1].getMiddleData(),
                   self.boardGrid[2][1].getMiddleData(),
                   self.boardGrid[0][1].getLowerData(),
                   self.boardGrid[1][1].getLowerData(),
                   self.boardGrid[2][1].getLowerData(),
                   
                   self.boardGrid[0][2].getUpperData(),
                   self.boardGrid[1][2].getUpperData(),
                   self.boardGrid[2][2].getUpperData(),
                   self.boardGrid[0][2].getMiddleData(),
                   self.boardGrid[1][2].getMiddleData(),
                   self.boardGrid[2][2].getMiddleData(),
                   self.boardGrid[0][2].getLowerData(),
                   self.boardGrid[1][2].getLowerData(),
                   self.boardGrid[2][2].getLowerData()
        )) 

class Player:
    def __init__(self, name, sign):
           self.name = name
           self.sign = sign

def updateBoard(y, x, boardObj, player):
   boardObj.board[y][x] = player.sign 

def getBoardFromGrid(superBoard, currentBoardX, currentBoardY):
    return superBoard.boardGrid[currentBoardX][currentBoardY]

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

print("Welcome to Ultimate Tic Tac Toe! To play, first enter two user names.")
p1 = Player("(X) " + input("Enter a name for player 1 (who will play as X): "), "X")
p2 = Player("(O) " + input("Enter a name for player 2 (who will play as O): "), "O")

print("If you don't know the rules of Ultimate Tic Tac Toe, read them on: \n https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe \n")

# Board variable which holds the normal boards
superBoard = SuperBoard()

print("Initial board:")
superBoard.getData()

print("Enter coordinates one by one. First the X, then the Y.")

winner = "-"
finished = False
currentBoard = getBoardFromGrid(superBoard, 1, 1)
currentBoardX = 1
currentBoardY = 1
metaBoard = Board()

while (not finished):

    # Player 1

    u1x = int(input(p1.name + " X: "))
    u1y = int(input(p1.name + " Y: "))
    while inputIsFalse(u1x, u1y, currentBoard):
        u1x = int(input(p1.name + " X: "))
        u1y = int(input(p1.name + " Y: "))
    
    updateBoard(u1y, u1x, currentBoard, p1)
    
    # check if the current board has a winner
    if checkWinner(currentBoard):
        print(p1.name + " has won this board!")
        currentBoard.getRawData()

        # Show who won the board
        for x in range(0,3):
            for y in range(0,3):
                currentBoard.board[y][x] = "X"

        # check if the entire game has been won
        updateBoard(currentBoardX, currentBoardY, metaBoard, p1)
        if checkWinner(metaBoard):
            print(p1.name + " has won the entire game!")
            break

        # select next board
        print(p2.name + ", which board do you want to play? Select X and Y coordinate:")
        u1x = input("X: ")
        u1y = input("Y: ")
        while(inputIsFalse(u1x, u1y, metaBoard))
            print("That board is already finished. Please choose again:")
            u1x = input("X: ")
            u1y = input("Y: ")

    currentBoard = getBoardFromGrid(superBoard, u1x, u1y)
    superBoard.getData()

    # Player 2

    u2x = int(input(p2.name + " X: "))
    u2y = int(input(p2.name + " Y: "))
    while inputIsFalse(u2x, u2y, currentBoard):
        u2x = int(input(p2.name + " X: "))
        u2y = int(input(p2.name + " Y: "))
    
    updateBoard(u2y, u2x, currentBoard, p2)
    
    # check if the current board has a winner
    if checkWinner(currentBoard):
        print(p2.name + " has won this board!")
        currentBoard.getRawData()

        # Show who won the board
        for x in range(0,3):
            for y in range(0,3):
                currentBoard.board[y][x] = "O"

        # check if the entire game has been won
        updateBoard(currentBoardX, currentBoardY, metaBoard, p2)
        if checkWinner(metaBoard):
            print(p2.name + " has won the entire game!")
            break

        # select next board
        print(p1.name + ", which board do you want to play? Select X and Y coordinate:")
        u2x = input("X: ")
        u2y = input("Y: ")
        while(inputIsFalse(u2x, u2y, metaBoard))
            print("That board is already finished. Please choose again:")
            u2x = input("X: ")
            u2y = input("Y: ")

    currentBoard = getBoardFromGrid(superBoard, u2x, u2y)
    superBoard.getData()

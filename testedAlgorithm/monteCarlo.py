import random
import ast

BoardSpot = []
BoardDisp = {}
Player = 0
TurnCount = 0
BoardSize = 3
Simulations = 200

def initBoard():
    global BoardSize
    global BoardSpot
    global BoardDisp
    count = 1
    while count<=(BoardSize * BoardSize):
        BoardDisp[count] = "-"
        count+=1

    temp = []
    x = "-"
    y = x * BoardSize
    z = (list(y))
    i = 0
    while i<BoardSize:
        temp.append(z)
        i+=1
    BoardSpot = temp
    return(BoardSpot)
    
def drawBoard(BoardSpot):
    board = boardDict(BoardSpot)
    disp = ""
    i = 1
    j = 0
    while i<=len(board):
        j = 0
        while j<BoardSize:
            disp = disp + "|"+str(board[i])+"|"
            j+=1
            i+=1
        disp= disp + "\n"
    boardDisplay =(disp)
    # boardDisplay = (f"|{board[1]}||{board[2]}||{board[3]}|\n|{board[4]}||{board[5]}||{board[6]}|\n|{board[7]}||{board[8]}||{board[9]}|")
    print(boardDisplay)
    
def gameStart():
    global BoardSpot
    print("Welcome! X plays first!\n")
    BoardSpot = initBoard()
    drawBoard(BoardSpot)
    playerPiece = 'x'
    cpuTurn(BoardSpot, playerPiece)
    
def checkWin(boardX):
    global Player
    board = boardDict(boardX)
    drawBoard(BoardSpot)
    #horizontal
    if((board[1] == 'x' and board[2] == 'x' and board[3] == 'x') 
    or (board[4] == 'x' and board[5] == 'x' and board[6] == 'x') 
    or (board[7] == 'x' and board[8] == 'x' and board[9] == 'x')):
        endGame('x')
    elif((board[1] == 'o' and board[2] == 'o' and board[3] == 'o') 
    or (board[4] == 'o' and board[5] == 'o' and board[6] == 'o') 
    or (board[7] == 'o' and board[8] == 'o' and board[9] == 'o')):
        endGame('o')
        
        #vertical
    elif((board[1] == 'x' and board[4] == 'x' and board[7] == 'x') 
    or (board[2] == 'x' and board[5] == 'x' and board[8] == 'x') 
    or (board[3] == 'x' and board[6] == 'x' and board[9] == 'x')):
        endGame('x')
        
    elif((board[1] == 'o' and board[4] == 'o' and board[7] == 'o') 
    or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o') 
    or (board[3] == 'o' and board[6] == 'o' and board[9] == 'o')):
        endGame('o')
        
        #diagnol
    elif((board[1] == 'x' and board[5] == 'x' and board[9] == 'x') 
    or (board[3] == 'x' and board[5] == 'x' and board[7] == 'x')):
        endGame('x')
        
    elif((board[1] == 'o' and board[5] == 'o' and board[9] == 'o') 
    or (board[3] == 'o' and board[5] == 'o' and board[7] == 'o')):
        endGame('o')
    
    elif(TurnCount == 9):
        endGame("Tie")
    else:
        Player+=1
        if(Player == 1):
            playerPiece = 'o'
            cpuTurn(BoardSpot,playerPiece)
        elif(Player > 1):
            Player = 0
            playerPiece = 'x'
            cpuTurn(BoardSpot,playerPiece)
        
def endGame(win):
    print("Winner is ", win)
    
def cpuMakesMove(bestMove):
    global TurnCount
    global BoardSpot
    BoardSpot = bestMove
    TurnCount+=1
    checkWin(BoardSpot)
    
def simulationBoard(board):
    simBoard = []
    for i in board:
        simBoard.append(i.copy())
    return simBoard

def getMoves(board,player):
    global BoardSize
    movesLeft = []
    
    for i in range(BoardSize):
        for j in range(BoardSize):
            if(board[i][j] == "-"):
                simBoard = simulationBoard(board)
                simBoard[i][j] = player
                movesLeft.append(simBoard)
    return movesLeft

def cpuTurn(BoardSpot, curPlayer):
    global BoardSize
    global Simulations
    evals = {}
    
    for x in range(Simulations):
        player = curPlayer
        simBoard = simulationBoard(BoardSpot)
        
        simulatedMoves = []
        moves = getMoves(simBoard,player)

        score = BoardSize*BoardSize
        
        while(moves != []):
            attempt = random.randint(1,len(moves))-1
            simBoard = moves[attempt]
            
            simulatedMoves.append(simBoard)
            
            result = cpuCheckWin(simBoard)
            
            if(result == player):
                break
            
            score-=1

            if(player == 'x'):
                player = 'o'
                opponent = 'x'
            else:
                player = 'x'
                opponent = 'o'
                
            moves = getMoves(simBoard,player)
            
        first = simulatedMoves[0]
        last = simulatedMoves[-1]
        
        firstKey = repr(first)
        
        result = cpuCheckWin(simBoard)
        if(player == result ):
            score *= -1
            
        if(firstKey in evals):
            evals[firstKey] += score
        else:
            evals[firstKey] = score
    bestMove = []
    bestScore = 0
    firstTurn = True
    
    for move, score in evals.items():
        
        if firstTurn == True or score > bestScore:
            bestScore = score
            bestMove = ast.literal_eval(move)
            firstTurn = False  
            
    cpuMakesMove(bestMove)
    
def boardDict(boardX):
    board = BoardDisp
    tempBoard = []
    for list in boardX:
        for value in list:
            tempBoard.append(value)
    i = 1
    while i <=len(board):
        board[i]=tempBoard[i-1]
        i+=1
    return board

def cpuCheckWin(boardX):
    
    board = boardDict(boardX)
    #horizontal
    if((board[1] == 'x' and board[2] == 'x' and board[3] == 'x') 
    or (board[4] == 'x' and board[5] == 'x' and board[6] == 'x') 
    or (board[7] == 'x' and board[8] == 'x' and board[9] == 'x')):
        return('x')
    elif((board[1] == 'o' and board[2] == 'o' and board[3] == 'o') 
    or (board[4] == 'o' and board[5] == 'o' and board[6] == 'o') 
    or (board[7] == 'o' and board[8] == 'o' and board[9] == 'o')):
        return('o')
        
        #vertical
    elif((board[1] == 'x' and board[4] == 'x' and board[7] == 'x') 
    or (board[2] == 'x' and board[5] == 'x' and board[8] == 'x') 
    or (board[3] == 'x' and board[6] == 'x' and board[9] == 'x')):
        return('x')
        
    elif((board[1] == 'o' and board[4] == 'o' and board[7] == 'o') 
    or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o') 
    or (board[3] == 'o' and board[6] == 'o' and board[9] == 'o')):
        return('o')
        
        #diagnol
    elif((board[1] == 'x' and board[5] == 'x' and board[9] == 'x') 
    or (board[3] == 'x' and board[5] == 'x' and board[7] == 'x')):
        return('x')
        
    elif((board[1] == 'o' and board[5] == 'o' and board[9] == 'o') 
    or (board[3] == 'o' and board[5] == 'o' and board[7] == 'o')):
        return('o')
    
    if(board[1] != '-' and board[2] != '-'  and board[3] != '-'
    and board[4] != '-'  and board[5] != '-'  and board[6] != '-' 
    and board[7] != '-'  and board[8] != '-'  and board[9]!= '-'):
        return('tie')

gameStart()
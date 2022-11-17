import random
import ast
import time

BoardSpot = []
BoardDisp = {}
Player = 0
TurnCount = 0
BoardSize = 4
Simulations = 200
startTime = time.time()
TurnTimes = []

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
    #horizontal
    if((board[1] == 'x' and board[2] == 'x' and board[3] == 'x' and board[4] == 'x') 
    or (board[5] == 'x' and board[6] == 'x' and board[7] == 'x' and board[8] == 'x') 
    or (board[9] == 'x' and board[10] == 'x' and board[11] == 'x' and board[12] == 'x')
    or (board[13] == 'x' and board[14] == 'x' and board[15] == 'x' and board[16] == 'x')):
        endGame('x')
    elif((board[1] == 'o' and board[2] == 'o' and board[3] == 'o' and board[4] == 'o') 
    or (board[5] == 'o' and board[6] == 'o' and board[7] == 'o' and board[8] == 'o') 
    or (board[9] == 'o' and board[10] == 'o' and board[11] == 'o' and board[12] == 'o')
    or (board[13] == 'o' and board[14] == 'o' and board[15] == 'o' and board[16] == 'o')):
        endGame('o')
        
        #vertical
    elif((board[1] == 'x' and board[5] == 'x' and board[9] == 'x' and board[13] == 'x') 
    or (board[2] == 'x' and board[6] == 'x' and board[10] == 'x' and board[14] == 'x') 
    or (board[3] == 'x' and board[7] == 'x' and board[11] == 'x' and board[15] == 'x')
    or (board[4] == 'x' and board[8] == 'x' and board[12] == 'x' and board[16] == 'x')):
        endGame('x')
        
    elif((board[1] == 'o' and board[5] == 'o' and board[9] == 'o' and board[13] == 'o') 
    or (board[2] == 'o' and board[6] == 'o' and board[10] == 'o' and board[14] == 'o') 
    or (board[3] == 'o' and board[7] == 'o' and board[11] == 'o' and board[15] == 'o')
    or (board[4] == 'o' and board[8] == 'o' and board[12] == 'o' and board[16] == 'o')):
        endGame('o')
        
        #diagnol
    elif((board[1] == 'x' and board[6] == 'x' and board[11] == 'x' and board[16] == 'x') 
    or (board[4] == 'x' and board[7] == 'x' and board[10] == 'x' and board[13] == 'x')):
        endGame('x')
        
    elif((board[1] == 'o' and board[6] == 'o' and board[11] == 'o' and board[16] == 'o') 
    or (board[4] == 'o' and board[7] == 'o' and board[10] == 'o' and board[13] == 'o')):
        endGame('o')
    
    elif(TurnCount == 16):
        endGame("Tie")
    else:
        if(Player == 0):
            Player = 1
            playerPiece = 'o'
            cpuTurn(BoardSpot,playerPiece)
        else:
            Player = 0
            playerPiece = 'x'
            cpuTurn(BoardSpot,playerPiece)
        
def endGame(win):
    drawBoard(BoardSpot)
    averageTime = 0
    endTime = time.time()
    totalTime = endTime - startTime
    i = 0
    while i <len(TurnTimes):
        averageTime+= TurnTimes[i]
        i+=1
    averageTime = averageTime/len(TurnTimes)
    print("Winner is ", win)
    print("Average Turn = ",averageTime)
    print("Total game: ", totalTime)
    
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
    turnTimeStart = time.time()
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
    turnTime = time.time() - turnTimeStart
    # print(turnTime)
    TurnTimes.append(turnTime)
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
    if((board[1] == 'x' and board[2] == 'x' and board[3] == 'x' and board[4] == 'x') 
    or (board[5] == 'x' and board[6] == 'x' and board[7] == 'x' and board[8] == 'x') 
    or (board[9] == 'x' and board[10] == 'x' and board[11] == 'x' and board[12] == 'x')
    or (board[13] == 'x' and board[14] == 'x' and board[15] == 'x' and board[16] == 'x')):
        return 'x'
    elif((board[1] == 'o' and board[2] == 'o' and board[3] == 'o' and board[4] == 'o') 
    or (board[5] == 'o' and board[6] == 'o' and board[7] == 'o' and board[8] == 'o') 
    or (board[9] == 'o' and board[10] == 'o' and board[11] == 'o' and board[12] == 'o')
    or (board[13] == 'o' and board[14] == 'o' and board[15] == 'o' and board[16] == 'o')):
        return 'o'
        
        #vertical
    elif((board[1] == 'x' and board[5] == 'x' and board[9] == 'x' and board[13] == 'x') 
    or (board[2] == 'x' and board[6] == 'x' and board[10] == 'x' and board[14] == 'x') 
    or (board[3] == 'x' and board[7] == 'x' and board[11] == 'x' and board[15] == 'x')
    or (board[4] == 'x' and board[8] == 'x' and board[12] == 'x' and board[16] == 'x')):
        return 'x'
        
    elif((board[1] == 'o' and board[5] == 'o' and board[9] == 'o' and board[13] == 'o') 
    or (board[2] == 'o' and board[6] == 'o' and board[10] == 'o' and board[14] == 'o') 
    or (board[3] == 'o' and board[7] == 'o' and board[11] == 'o' and board[15] == 'o')
    or (board[4] == 'o' and board[8] == 'o' and board[12] == 'o' and board[16] == 'o')):
        return 'o'
        
        #diagnol
    elif((board[1] == 'x' and board[6] == 'x' and board[11] == 'x' and board[16] == 'x') 
    or (board[4] == 'x' and board[7] == 'x' and board[10] == 'x' and board[13] == 'x')):
        return 'x'
        
    elif((board[1] == 'o' and board[6] == 'o' and board[11] == 'o' and board[16] == 'o') 
    or (board[4] == 'o' and board[7] == 'o' and board[10] == 'o' and board[13] == 'o')):
        return 'o'
    
    if(board[1] != '-' and board[2] != '-'  and board[3] != '-' and board[4] != '-'
    and board[5] != '-'  and board[6] != '-'  and board[7] != '-' and board[8] != '-'
    and board[9] != '-'  and board[10] != '-'  and board[11]!= '-' and board[12] != '-'
    and board[13] != '-'  and board[14] != '-'  and board[15]!= '-' and board[16] != '-'):
        return('tie')

gameStart()
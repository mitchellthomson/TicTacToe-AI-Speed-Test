import random
import ast

BoardSpot = []
BoardDisp = {}
Player = 0
TurnCount = 0
BoardSize = 4
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
    
def checkWin():
    global Player
    drawBoard(BoardSpot)
    #horizontal
    if((BoardSpot[1] == 'x' and BoardSpot[2] == 'x' and BoardSpot[3] == 'x' and BoardSpot[4] == 'x') 
    or (BoardSpot[5] == 'x' and BoardSpot[6] == 'x' and BoardSpot[7] == 'x' and BoardSpot[8] == 'x') 
    or (BoardSpot[9] == 'x' and BoardSpot[10] == 'x' and BoardSpot[11] == 'x' and BoardSpot[12] == 'x')
    or (BoardSpot[13] == 'x' and BoardSpot[14] == 'x' and BoardSpot[15] == 'x' and BoardSpot[16] == 'x')):
        endGame('x')
    elif((BoardSpot[1] == 'o' and BoardSpot[2] == 'o' and BoardSpot[3] == 'o' and BoardSpot[4] == 'o') 
    or (BoardSpot[5] == 'o' and BoardSpot[6] == 'o' and BoardSpot[7] == 'o' and BoardSpot[8] == 'o') 
    or (BoardSpot[9] == 'o' and BoardSpot[10] == 'o' and BoardSpot[11] == 'o' and BoardSpot[12] == 'o')
    or (BoardSpot[13] == 'o' and BoardSpot[14] == 'o' and BoardSpot[15] == 'o' and BoardSpot[16] == 'o')):
        endGame('o')
        
        #vertical
    elif((BoardSpot[1] == 'x' and BoardSpot[5] == 'x' and BoardSpot[9] == 'x' and BoardSpot[13] == 'x') 
    or (BoardSpot[2] == 'x' and BoardSpot[6] == 'x' and BoardSpot[10] == 'x' and BoardSpot[14] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[7] == 'x' and BoardSpot[11] == 'x' and BoardSpot[15] == 'x')
    or (BoardSpot[4] == 'x' and BoardSpot[8] == 'x' and BoardSpot[12] == 'x' and BoardSpot[16] == 'x')):
        endGame('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[5] == 'o' and BoardSpot[9] == 'o' and BoardSpot[13] == 'o') 
    or (BoardSpot[2] == 'o' and BoardSpot[6] == 'o' and BoardSpot[10] == 'o' and BoardSpot[14] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[7] == 'o' and BoardSpot[11] == 'o' and BoardSpot[15] == 'o')
    or (BoardSpot[4] == 'o' and BoardSpot[8] == 'o' and BoardSpot[12] == 'o' and BoardSpot[16] == 'o')):
        endGame('o')
        
        #diagnol
    elif((BoardSpot[1] == 'x' and BoardSpot[6] == 'x' and BoardSpot[11] == 'x' and BoardSpot[16] == 'x') 
    or (BoardSpot[4] == 'x' and BoardSpot[7] == 'x' and BoardSpot[10] == 'x' and BoardSpot[13] == 'x')):
        endGame('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[6] == 'o' and BoardSpot[11] == 'o' and BoardSpot[16] == 'o') 
    or (BoardSpot[4] == 'o' and BoardSpot[7] == 'o' and BoardSpot[10] == 'o' and BoardSpot[13] == 'o')):
        endGame('o')
    
    elif(TurnCount == 16):
        endGame("Tie")
    else:
        if(Player == 0):
            Player = 1
            playerPiece = 'o'
            cpuTurn(playerPiece)
        else:
            Player = 0
            playerPiece = 'x'
            cpuTurn(playerPiece)
        
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

def cpuCheckWin():
    #horizontal
    if((BoardSpot[1] == 'x' and BoardSpot[2] == 'x' and BoardSpot[3] == 'x' and BoardSpot[4] == 'x') 
    or (BoardSpot[5] == 'x' and BoardSpot[6] == 'x' and BoardSpot[7] == 'x' and BoardSpot[8] == 'x') 
    or (BoardSpot[9] == 'x' and BoardSpot[10] == 'x' and BoardSpot[11] == 'x' and BoardSpot[12] == 'x')
    or (BoardSpot[13] == 'x' and BoardSpot[14] == 'x' and BoardSpot[15] == 'x' and BoardSpot[16] == 'x')):
        return 'x'
    elif((BoardSpot[1] == 'o' and BoardSpot[2] == 'o' and BoardSpot[3] == 'o' and BoardSpot[4] == 'o') 
    or (BoardSpot[5] == 'o' and BoardSpot[6] == 'o' and BoardSpot[7] == 'o' and BoardSpot[8] == 'o') 
    or (BoardSpot[9] == 'o' and BoardSpot[10] == 'o' and BoardSpot[11] == 'o' and BoardSpot[12] == 'o')
    or (BoardSpot[13] == 'o' and BoardSpot[14] == 'o' and BoardSpot[15] == 'o' and BoardSpot[16] == 'o')):
        return 'o'
        
        #vertical
    elif((BoardSpot[1] == 'x' and BoardSpot[5] == 'x' and BoardSpot[9] == 'x' and BoardSpot[13] == 'x') 
    or (BoardSpot[2] == 'x' and BoardSpot[6] == 'x' and BoardSpot[10] == 'x' and BoardSpot[14] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[7] == 'x' and BoardSpot[11] == 'x' and BoardSpot[15] == 'x')
    or (BoardSpot[4] == 'x' and BoardSpot[8] == 'x' and BoardSpot[12] == 'x' and BoardSpot[16] == 'x')):
        return 'x'
        
    elif((BoardSpot[1] == 'o' and BoardSpot[5] == 'o' and BoardSpot[9] == 'o' and BoardSpot[13] == 'o') 
    or (BoardSpot[2] == 'o' and BoardSpot[6] == 'o' and BoardSpot[10] == 'o' and BoardSpot[14] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[7] == 'o' and BoardSpot[11] == 'o' and BoardSpot[15] == 'o')
    or (BoardSpot[4] == 'o' and BoardSpot[8] == 'o' and BoardSpot[12] == 'o' and BoardSpot[16] == 'o')):
        return 'o'
        
        #diagnol
    elif((BoardSpot[1] == 'x' and BoardSpot[6] == 'x' and BoardSpot[11] == 'x' and BoardSpot[16] == 'x') 
    or (BoardSpot[4] == 'x' and BoardSpot[7] == 'x' and BoardSpot[10] == 'x' and BoardSpot[13] == 'x')):
        return 'x'
        
    elif((BoardSpot[1] == 'o' and BoardSpot[6] == 'o' and BoardSpot[11] == 'o' and BoardSpot[16] == 'o') 
    or (BoardSpot[4] == 'o' and BoardSpot[7] == 'o' and BoardSpot[10] == 'o' and BoardSpot[13] == 'o')):
        return 'o'
    
    if(BoardSpot[1] != '-' and BoardSpot[2] != '-'  and BoardSpot[3] != '-' and BoardSpot[4] != '-'
    and BoardSpot[5] != '-'  and BoardSpot[6] != '-'  and BoardSpot[7] != '-' and BoardSpot[8] != '-'
    and BoardSpot[9] != '-'  and BoardSpot[10] != '-'  and BoardSpot[11]!= '-' and BoardSpot[12] != '-'
    and BoardSpot[13] != '-'  and BoardSpot[14] != '-'  and BoardSpot[15]!= '-' and BoardSpot[16] != '-'):
        return('tie')

gameStart()
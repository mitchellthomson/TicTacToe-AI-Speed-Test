import random
import ast
import time

BoardSpot = []
BoardDisp = {}
Player = 0
TurnCount = 0
BoardSize = 10
Simulations = 200
startTime = time.time()
TurnTimes = []
moveCount = 0

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
    BoardSpot = initBoard()
    drawBoard(BoardSpot)
    playerPiece = 'x'
    cpuTurn(BoardSpot, playerPiece)
    
def checkWin(boardX):
    global Player
    board = boardDict(boardX)
    # drawBoard(BoardSpot)
    
    #horizontal
    if((board[1] == 'x' and board[2] == 'x' and board[3] == 'x' and board[4] == 'x' and board[5] == 'x' and board[6] == 'x' and board[7] == 'x' and board[8] == 'x' and board[9] == 'x' and board[10] == 'x') 
    or (board[11] == 'x' and board[12] == 'x' and board[13] == 'x' and board[14] == 'x' and board[15] == 'x' and board[16] == 'x' and board[17] == 'x' and board[18] == 'x' and board[19] == 'x' and board[20] == 'x') 
    or (board[21] == 'x' and board[22] == 'x' and board[23] == 'x' and board[24] == 'x' and board[25] == 'x' and board[26] == 'x' and board[27] == 'x' and board[28] == 'x' and board[29] == 'x' and board[30] == 'x')
    or (board[31] == 'x' and board[32] == 'x' and board[33] == 'x' and board[34] == 'x' and board[35] == 'x' and board[36] == 'x' and board[37] == 'x' and board[38] == 'x' and board[39] == 'x' and board[40] == 'x')
    or (board[41] == 'x' and board[42] == 'x' and board[43] == 'x' and board[44] == 'x' and board[45] == 'x' and board[46] == 'x' and board[47] == 'x' and board[48] == 'x' and board[49] == 'x' and board[50] == 'x')
    or (board[51] == 'x' and board[52] == 'x' and board[53] == 'x' and board[54] == 'x' and board[55] == 'x' and board[56] == 'x' and board[57] == 'x' and board[58] == 'x' and board[59] == 'x' and board[60] == 'x')
    or (board[61] == 'x' and board[62] == 'x' and board[63] == 'x' and board[64] == 'x' and board[65] == 'x' and board[66] == 'x' and board[67] == 'x' and board[68] == 'x' and board[69] == 'x' and board[70] == 'x')
    or (board[71] == 'x' and board[72] == 'x' and board[73] == 'x' and board[74] == 'x' and board[75] == 'x' and board[76] == 'x' and board[77] == 'x' and board[78] == 'x' and board[79] == 'x' and board[80] == 'x')
    or (board[81] == 'x' and board[82] == 'x' and board[83] == 'x' and board[84] == 'x' and board[85] == 'x' and board[86] == 'x' and board[87] == 'x' and board[88] == 'x' and board[89] == 'x' and board[90] == 'x')
    or (board[91] == 'x' and board[92] == 'x' and board[93] == 'x' and board[94] == 'x' and board[95] == 'x' and board[96] == 'x' and board[97] == 'x' and board[98] == 'x' and board[99] == 'x' and board[100] == 'x')):
        return 'x'
    
    if((board[1] == 'o' and board[2] == 'o' and board[3] == 'o' and board[4] == 'o' and board[5] == 'o' and board[6] == 'o' and board[7] == 'o' and board[8] == 'o' and board[9] == 'o' and board[10] == 'o') 
    or (board[11] == 'o' and board[12] == 'o' and board[13] == 'o' and board[14] == 'o' and board[15] == 'o' and board[16] == 'o' and board[17] == 'o' and board[18] == 'o' and board[19] == 'o' and board[20] == 'o') 
    or (board[21] == 'o' and board[22] == 'o' and board[23] == 'o' and board[24] == 'o' and board[25] == 'o' and board[26] == 'o' and board[27] == 'o' and board[28] == 'o' and board[29] == 'o' and board[30] == 'o')
    or (board[31] == 'o' and board[32] == 'o' and board[33] == 'o' and board[34] == 'o' and board[35] == 'o' and board[36] == 'o' and board[37] == 'o' and board[38] == 'o' and board[39] == 'o' and board[40] == 'o')
    or (board[41] == 'o' and board[42] == 'o' and board[43] == 'o' and board[44] == 'o' and board[45] == 'o' and board[46] == 'o' and board[47] == 'o' and board[48] == 'o' and board[49] == 'o' and board[50] == 'o')
    or (board[51] == 'o' and board[52] == 'o' and board[53] == 'o' and board[54] == 'o' and board[55] == 'o' and board[56] == 'o' and board[57] == 'o' and board[58] == 'o' and board[59] == 'o' and board[60] == 'o')
    or (board[61] == 'o' and board[62] == 'o' and board[63] == 'o' and board[64] == 'o' and board[65] == 'o' and board[66] == 'o' and board[67] == 'o' and board[68] == 'o' and board[69] == 'o' and board[70] == 'o')
    or (board[71] == 'o' and board[72] == 'o' and board[73] == 'o' and board[74] == 'o' and board[75] == 'o' and board[76] == 'o' and board[77] == 'o' and board[78] == 'o' and board[79] == 'o' and board[80] == 'o')
    or (board[81] == 'o' and board[82] == 'o' and board[83] == 'o' and board[84] == 'o' and board[85] == 'o' and board[86] == 'o' and board[87] == 'o' and board[88] == 'o' and board[89] == 'o' and board[90] == 'o')
    or (board[91] == 'o' and board[92] == 'o' and board[93] == 'o' and board[94] == 'o' and board[95] == 'o' and board[96] == 'o' and board[97] == 'o' and board[98] == 'o' and board[99] == 'o' and board[100] == 'o')):
        return 'o'
    
        #vertical
    elif((board[1] == 'x' and board[11] == 'x' and board[21] == 'x' and board[31] == 'x' and board[41] == 'x' and board[51] == 'x' and board[61] == 'x' and board[71] == 'x' and board[81] == 'x' and board[91] == 'x') 
    or (board[2] == 'x' and board[12] == 'x' and board[22] == 'x' and board[32] == 'x' and board[42] == 'x' and board[52] == 'x' and board[62] == 'x' and board[72] == 'x' and board[82] == 'x' and board[92] == 'x') 
    or (board[3] == 'x' and board[13] == 'x' and board[23] == 'x' and board[33] == 'x' and board[43] == 'x' and board[53] == 'x' and board[63] == 'x' and board[73] == 'x' and board[83] == 'x' and board[93] == 'x')
    or (board[4] == 'x' and board[14] == 'x' and board[24] == 'x' and board[34] == 'x' and board[44] == 'x' and board[54] == 'x' and board[64] == 'x' and board[74] == 'x' and board[84] == 'x' and board[94] == 'x')
    or (board[5] == 'x' and board[15] == 'x' and board[25] == 'x' and board[35] == 'x' and board[45] == 'x' and board[55] == 'x' and board[65] == 'x' and board[75] == 'x' and board[85] == 'x' and board[95] == 'x')
    or (board[6] == 'x' and board[16] == 'x' and board[26] == 'x' and board[36] == 'x' and board[46] == 'x' and board[56] == 'x' and board[66] == 'x' and board[76] == 'x' and board[86] == 'x' and board[96] == 'x')
    or (board[7] == 'x' and board[17] == 'x' and board[27] == 'x' and board[37] == 'x' and board[47] == 'x' and board[57] == 'x' and board[67] == 'x' and board[77] == 'x' and board[87] == 'x' and board[97] == 'x')
    or (board[8] == 'x' and board[18] == 'x' and board[28] == 'x' and board[38] == 'x' and board[48] == 'x' and board[58] == 'x' and board[68] == 'x' and board[78] == 'x' and board[88] == 'x' and board[98] == 'x')
    or (board[9] == 'x' and board[19] == 'x' and board[29] == 'x' and board[39] == 'x' and board[49] == 'x' and board[59] == 'x' and board[69] == 'x' and board[79] == 'x' and board[89] == 'x' and board[99] == 'x')
    or (board[10] == 'x' and board[20] == 'x' and board[30] == 'x' and board[40] == 'x' and board[50] == 'x' and board[60] == 'x' and board[70] == 'x' and board[80] == 'x' and board[90] == 'x' and board[100] == 'x')):
        return 'x'
    
    elif((board[1] == 'o' and board[11] == 'o' and board[21] == 'o' and board[31] == 'o' and board[41] == 'o' and board[51] == 'o' and board[61] == 'o' and board[71] == 'o' and board[81] == 'o' and board[91] == 'o') 
    or (board[2] == 'o' and board[12] == 'o' and board[22] == 'o' and board[32] == 'o' and board[42] == 'o' and board[52] == 'o' and board[62] == 'o' and board[72] == 'o' and board[82] == 'o' and board[92] == 'o') 
    or (board[3] == 'o' and board[13] == 'o' and board[23] == 'o' and board[33] == 'o' and board[43] == 'o' and board[53] == 'o' and board[63] == 'o' and board[73] == 'o' and board[83] == 'o' and board[93] == 'o')
    or (board[4] == 'o' and board[14] == 'o' and board[24] == 'o' and board[34] == 'o' and board[44] == 'o' and board[54] == 'o' and board[64] == 'o' and board[74] == 'o' and board[84] == 'o' and board[94] == 'o')
    or (board[5] == 'o' and board[15] == 'o' and board[25] == 'o' and board[35] == 'o' and board[45] == 'o' and board[55] == 'o' and board[65] == 'o' and board[75] == 'o' and board[85] == 'o' and board[95] == 'o')
    or (board[6] == 'o' and board[16] == 'o' and board[26] == 'o' and board[36] == 'o' and board[46] == 'o' and board[56] == 'o' and board[66] == 'o' and board[76] == 'o' and board[86] == 'o' and board[96] == 'o')
    or (board[7] == 'o' and board[17] == 'o' and board[27] == 'o' and board[37] == 'o' and board[47] == 'o' and board[57] == 'o' and board[67] == 'o' and board[77] == 'o' and board[87] == 'o' and board[97] == 'o')
    or (board[8] == 'o' and board[18] == 'o' and board[28] == 'o' and board[38] == 'o' and board[48] == 'o' and board[58] == 'o' and board[68] == 'o' and board[78] == 'o' and board[88] == 'o' and board[98] == 'o')
    or (board[9] == 'o' and board[19] == 'o' and board[29] == 'o' and board[39] == 'o' and board[49] == 'o' and board[59] == 'o' and board[69] == 'o' and board[79] == 'o' and board[89] == 'o' and board[99] == 'o')
    or (board[10] == 'o' and board[20] == 'o' and board[30] == 'o' and board[40] == 'o' and board[50] == 'o' and board[60] == 'o' and board[70] == 'o' and board[80] == 'o' and board[90] == 'o' and board[100] == 'o')):
        return 'x'
        
        #diagnol
    elif((board[1] == 'x' and board[12] == 'x' and board[23] == 'x' and board[34] == 'x' and board[45] == 'x' and board[56] == 'x' and board[67] == 'x' and board[78] == 'x' and board[89] == 'x' and board[100] == 'x')
    or (board[10] == 'x' and board[19] == 'x' and board[28] == 'x' and board[37] == 'x' and board[46] == 'x' and board[55] == 'x' and board[64] == 'x' and board[73] == 'x' and board[82] == 'x' and board[91] == 'x')):
        return 'x'
        
    elif((board[1] == 'o' and board[12] == 'o' and board[23] == 'o' and board[34] == 'o' and board[45] == 'o' and board[56] == 'o' and board[67] == 'o' and board[78] == 'o' and board[89] == 'o' and board[100] == 'o')
    or (board[10] == 'o' and board[19] == 'o' and board[28] == 'o' and board[37] == 'o' and board[46] == 'o' and board[55] == 'o' and board[64] == 'o' and board[73] == 'o' and board[82] == 'o' and board[91] == 'o')):
        return 'o'
    
    elif(TurnCount == 100):
        endGame("Tie")
    else:
        if(Player == 0):
            Player = 1
            playerPiece = 'o'
            cpuTurn(BoardSpot, playerPiece)
        else:
            Player = 0
            playerPiece = 'x'
            cpuTurn(BoardSpot, playerPiece)
        
def endGame(win):
    global moveCount
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
    print("Total Calcs Made = ", moveCount)
    
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
    global moveCount
    turnTimeStart = time.time()
    global BoardSize
    global Simulations
    evals = {}
    
    
    for x in range(Simulations):
        moveCount+=1
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
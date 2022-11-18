import time

BoardSpot = {1 : "-",2 : "x",3 : "-",4 : "x",5 : "-",6 : "-",7 : "o",8 : "-",9 : "x",10 : "o",11 : "-",12 : "-",13 : "-",14 : "o",15 : "-",16 : "-"}
Player = 0
TurnCount = 6
startTime = time.time()
TurnTimes = []
movecount = 0

def drawBoard(BoardSpot):
    boardDisplay = (f"|{BoardSpot[1]}||{BoardSpot[2]}||{BoardSpot[3]}||{BoardSpot[4]}|\n|{BoardSpot[5]}||{BoardSpot[6]}||{BoardSpot[7]}||{BoardSpot[8]}|\n|{BoardSpot[9]}||{BoardSpot[10]}||{BoardSpot[11]}||{BoardSpot[12]}|\n|{BoardSpot[13]}||{BoardSpot[14]}||{BoardSpot[15]}||{BoardSpot[16]}|\n")
    print(boardDisplay)
    
def gameStart():
    drawBoard(BoardSpot)
    playerPiece = 'x'
    cpuTurn(playerPiece)
    

def checkWin():
    global Player
    # drawBoard(BoardSpot)
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
    global movecount
    averageTime = 0
    print("Winner is ", win)
    endTime = time.time()
    totalTime = endTime - startTime
    i = 0
    while i <len(TurnTimes):
        averageTime+= TurnTimes[i]
        i+=1
    averageTime = averageTime/len(TurnTimes)
    print("Total game: ", totalTime)
    print("Average Turn = ",averageTime)
    # print("Total Calcs Made = ", movecount)
    
def cpuMakesMove(bestMove, playerPiece):
    global TurnCount
    BoardSpot[bestMove] = playerPiece
    TurnCount+=1
    checkWin()
    
def cpuTurn(playerPiece):
    turnTimeStart = time.time()
    bestScore = -8000
    bestMove = 0
    i = 1
    while(i<=len(BoardSpot)):
        if(BoardSpot[i] == "-"):
            BoardSpot[i] = playerPiece
            score = miniMax(BoardSpot,0,False, playerPiece)
            BoardSpot[i] = "-"
            
            if(score > bestScore):
                bestScore = score
                bestMove = i
            
        i+=1
    turnTime = time.time() - turnTimeStart
    # print(turnTime)
    TurnTimes.append(turnTime)
    cpuMakesMove(bestMove,playerPiece)

def miniMax(BoardSpot, depth, isMaximizing, playerPiece):
    global movecount
    movecount+=1
    winCheck = cpuCheckWin()
    depth+=1
    
    if(playerPiece == 'x'):
        opponentPiece = 'o'
        if(winCheck == 'x'):
            return 100
        elif(winCheck == 'o'):
            return -100
        elif(winCheck == 'tie'):
            return 0
        
    if(playerPiece == 'o'):
        opponentPiece = 'x'
        if(winCheck == 'x'):
            return -100
        elif(winCheck == 'o'):
            return 100
        elif(winCheck == 'tie'):
            return 0
        
    if(isMaximizing):
        bestScore = -1000
        
        i = 1
        while(i<=len(BoardSpot)):
            if(BoardSpot[i] == "-"):
                BoardSpot[i] = playerPiece
                score = miniMax(BoardSpot,depth,False,playerPiece)
                BoardSpot[i] = "-"
                
                if(score > bestScore):
                    bestScore = score
            i+=1
        return bestScore
    
    else:
        bestScore = 800
        i = 1
        while(i<=len(BoardSpot)):
            if(BoardSpot[i] == "-"):
                BoardSpot[i] = opponentPiece
                score = miniMax(BoardSpot,depth,True,playerPiece)
                BoardSpot[i] = "-"
                
                if(score < bestScore):
                    bestScore = score
            i+=1
        return bestScore
    
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
BoardSpot = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
Player = 0
TurnCount = 0

def drawBoard(BoardSpot):
    boardDisplay = (f"|{BoardSpot[1]}||{BoardSpot[2]}||{BoardSpot[3]}|\n|{BoardSpot[4]}||{BoardSpot[5]}||{BoardSpot[6]}|\n|{BoardSpot[7]}||{BoardSpot[8]}||{BoardSpot[9]}|")
    print(boardDisplay)
    
def gameStart():
    print("Welcome! X plays first!\n")
    drawBoard(BoardSpot)
    playerPiece = 'x'
    playTurn(playerPiece)
    
def playTurn(playerPiece):
    global Player
    global TurnCount
    print("Play your turn: "+ playerPiece)
    
    while True:
        move = input()
        if(move in ('1', '2', '3', '4', '5', '6', '7', '8', '9') and BoardSpot[int(move)] == '-'):
            break
        else:
            print("\nInvalid Move Try AGAIN: ")
            
    BoardSpot[int(move)] = playerPiece
    TurnCount+=1
    checkWin()

def checkWin():
    global Player
    drawBoard(BoardSpot)
    #horizontal
    if((BoardSpot[1] == 'x' and BoardSpot[2] == 'x' and BoardSpot[3] == 'x') 
    or (BoardSpot[4] == 'x' and BoardSpot[5] == 'x' and BoardSpot[6] == 'x') 
    or (BoardSpot[7] == 'x' and BoardSpot[8] == 'x' and BoardSpot[9] == 'x')):
        endGame('x')
    elif((BoardSpot[1] == 'o' and BoardSpot[2] == 'o' and BoardSpot[3] == 'o') 
    or (BoardSpot[4] == 'o' and BoardSpot[5] == 'o' and BoardSpot[6] == 'o') 
    or (BoardSpot[7] == 'o' and BoardSpot[8] == 'o' and BoardSpot[9] == 'o')):
        endGame('o')
        
        #vertical
    elif((BoardSpot[1] == 'x' and BoardSpot[4] == 'x' and BoardSpot[7] == 'x') 
    or (BoardSpot[2] == 'x' and BoardSpot[5] == 'x' and BoardSpot[8] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[6] == 'x' and BoardSpot[9] == 'x')):
        endGame('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[4] == 'o' and BoardSpot[7] == 'o') 
    or (BoardSpot[2] == 'o' and BoardSpot[5] == 'o' and BoardSpot[8] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[6] == 'o' and BoardSpot[9] == 'o')):
        endGame('o')
        
        #diagnol
    elif((BoardSpot[1] == 'x' and BoardSpot[5] == 'x' and BoardSpot[9] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[5] == 'x' and BoardSpot[7] == 'x')):
        endGame('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[5] == 'o' and BoardSpot[9] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[5] == 'o' and BoardSpot[7] == 'o')):
        endGame('o')
    
    elif(TurnCount == 9):
        endGame("Tie")
    else:
        Player+=1
        if(Player == 1):
            cpuTurn()
        elif(Player > 1):
            Player = 0
            playerPiece = 'x'
            playTurn(playerPiece)
        
def endGame(win):
    print("Winner is ", win)
    
def cpuMakesMove(bestMove):
    global TurnCount
    BoardSpot[bestMove] = 'o'
    print(bestMove)
    TurnCount+=1
    checkWin()
    
def cpuTurn():
    i = 1
    score = 0
    while(i<=len(BoardSpot)):
        if(BoardSpot[i] == "-"):
            BoardSpot[i] = "o"
            val = maxAlphaBeta(BoardSpot,-2,2)
            score = val[0]
            bestMove = val[1]
            BoardSpot[i] = "-"
            
        i+=1
    print(score)
    cpuMakesMove(bestMove)

def maxAlphaBeta(BoardSpot, alpha, beta):
    maxv = -2
    bestMove = 0
    
    winCheck = cpuCheckWin()
    if(winCheck == 'x'):
        return -100
    elif(winCheck == 'o'):
        return 100
    elif(winCheck == 'tie'):
        return 0
        
    i = 1
    while(i<=len(BoardSpot)):
        if(BoardSpot[i] == "-"):
            BoardSpot[i] = "o"
            val = minAlphaBeta(BoardSpot,alpha,beta)
            score = val[0]
            m = val[1]
            BoardSpot[i] = "-"
            
            if(score > maxv):
                maxv = score
                bestMove = m
                
            if(maxv >= beta):
                return maxv, bestMove
            if(maxv > alpha):
                alpha = maxv
        i+=1
    val[0]=maxv
    val[1]=bestMove
    return val
    
def minAlphaBeta(BoardSpot, alpha, beta):
    minv = 2
    bestMove = 0
    
    winCheck = cpuCheckWin()
    if(winCheck == 'x'):
        return -100
    elif(winCheck == 'o'):
        return 100
    elif(winCheck == 'tie'):
        return 0
        
    i = 1
    while(i<=len(BoardSpot)):
        if(BoardSpot[i] == "-"):
            BoardSpot[i] = "o"
            val = maxAlphaBeta(BoardSpot,alpha,beta)
            score = val[0]
            m = val[1]
            BoardSpot[i] = "-"
            
            if(score < minv):
                minv = score
                bestMove = m
                
            if(minv <= alpha):
                return minv, bestMove
            
            if(minv < beta):
                beta = minv
        i+=1
    val[0]=minv
    val[1]=bestMove
    return val
    
def cpuCheckWin():
    #horizontal
    if((BoardSpot[1] == 'x' and BoardSpot[2] == 'x' and BoardSpot[3] == 'x') 
    or (BoardSpot[4] == 'x' and BoardSpot[5] == 'x' and BoardSpot[6] == 'x') 
    or (BoardSpot[7] == 'x' and BoardSpot[8] == 'x' and BoardSpot[9] == 'x')):
        return('x')
    elif((BoardSpot[1] == 'o' and BoardSpot[2] == 'o' and BoardSpot[3] == 'o') 
    or (BoardSpot[4] == 'o' and BoardSpot[5] == 'o' and BoardSpot[6] == 'o') 
    or (BoardSpot[7] == 'o' and BoardSpot[8] == 'o' and BoardSpot[9] == 'o')):
        return('o')
        
        #vertical
    elif((BoardSpot[1] == 'x' and BoardSpot[4] == 'x' and BoardSpot[7] == 'x') 
    or (BoardSpot[2] == 'x' and BoardSpot[5] == 'x' and BoardSpot[8] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[6] == 'x' and BoardSpot[9] == 'x')):
        return('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[4] == 'o' and BoardSpot[7] == 'o') 
    or (BoardSpot[2] == 'o' and BoardSpot[5] == 'o' and BoardSpot[8] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[6] == 'o' and BoardSpot[9] == 'o')):
        return('o')
        
        #diagnol
    elif((BoardSpot[1] == 'x' and BoardSpot[5] == 'x' and BoardSpot[9] == 'x') 
    or (BoardSpot[3] == 'x' and BoardSpot[5] == 'x' and BoardSpot[7] == 'x')):
        return('x')
        
    elif((BoardSpot[1] == 'o' and BoardSpot[5] == 'o' and BoardSpot[9] == 'o') 
    or (BoardSpot[3] == 'o' and BoardSpot[5] == 'o' and BoardSpot[7] == 'o')):
        return('o')
    
    if(BoardSpot[1] != '-' and BoardSpot[2] != '-'  and BoardSpot[3] != '-'
    and BoardSpot[4] != '-'  and BoardSpot[5] != '-'  and BoardSpot[6] != '-' 
    and BoardSpot[7] != '-'  and BoardSpot[8] != '-'  and BoardSpot[9]!= '-'):
        return('tie')

gameStart()
import time
import math
import random
import sys
BoardSpot = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
Player = 0
TurnCount = 0
Simulate = 0
gameStartTime = 0
startTime = 0
gameTimes = []
count = 0

def drawBoard(BoardSpot):
    boardDisplay = (f"|{BoardSpot[1]}||{BoardSpot[2]}||{BoardSpot[3]}|\n|{BoardSpot[4]}||{BoardSpot[5]}||{BoardSpot[6]}|\n|{BoardSpot[7]}||{BoardSpot[8]}||{BoardSpot[9]}|")
    print(boardDisplay+"\n")
    
def reset():
    global TurnCount
    global gameStartTime
    i = 1
    while i <=(len(BoardSpot)):
        BoardSpot[i] = '-'
        i+=1
    TurnCount = 0
    gameStartTime = time.time()
    gameStart()
    
def gameStart():
    global Player
    Player = random.choice([0, 1])
    if(Player == 0):
        playerPiece = 'x'
    else:
        playerPiece = 'o'
    firstTurn(playerPiece)
    
def firstTurn(playerPiece):
    move = random.randint(1,9)
    cpuMakesMove(move, BoardSpot,playerPiece)
    
def checkWin(BoardSpot,TurnCount=0):
    drawBoard(BoardSpot)
    
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

    elif(TurnCount == 9 or  all([v != '-' for v in BoardSpot.values()])):
        return("Tie")
    else:
        return None
    
def endGame(win):
    global count
    global Simulate
    Simulate-=1
    print("Winner is ", win)
    endTime = time.time()
    totalTime = endTime - gameStartTime
    gameTimes.append(totalTime)
    if(Simulate > 0):
        reset()
    else:
        endGame = time.time()
        total = endGame - startTime
        averageTime = 0
        
        i = 0
        while(i<len(gameTimes)):
            averageTime+=i
            i+=1
        averageTime = averageTime/1000
        print("Time for simulation = ", total )
        print("Average time of games = ", averageTime)
        print("Total Calcs made = ", count)
    
def cpuMakesMove(bestMove, BoardSpot, playerPiece):
    global TurnCount
    BoardSpot[bestMove] = playerPiece
    TurnCount+=1
    win_results = checkWin(BoardSpot, TurnCount)
    if win_results is None:
        if(playerPiece == 'x'):
            playerPiece = 'o'
            cpuTurn(BoardSpot, playerPiece)
        else:
            playerPiece = 'x'
            cpuTurn(BoardSpot, playerPiece)
    else:
        endGame(win_results)
    
def cpuTurn(BoardSpot, playerPiece):
    turnTimeStart = time.time()
    bestScore = -8000
    bestMove = 0
    i = 1
    print(len(BoardSpot))
    while(i<=len(BoardSpot)):
        if(BoardSpot[i] == "-"):
            BoardSpot[i] = playerPiece
            score = miniMax(BoardSpot,3,False,float('-inf'),float('inf'),playerPiece)
            BoardSpot[i] = "-"   
            if(score > bestScore):
                bestScore = score
                bestMove = i
            
        i+=1
    # turnTime = time.time() - turnTimeStart
    
    # TurnTimes.append(turnTime)
    cpuMakesMove(bestMove, BoardSpot,playerPiece)

def miniMax(BoardSpot, depth, isMaximizing,alpha,beta,playerPiece):
    global count
    count+=1
    winCheck = checkWin(BoardSpot)
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
        i = 1
        bestScore = float('-inf')
        while(i<=len(BoardSpot)):
            if(BoardSpot[i] == "-"):
                BoardSpot[i] = playerPiece
                score = miniMax(BoardSpot,depth-1,False,alpha,beta,playerPiece)
                BoardSpot[i] = "-"
                bestScore = max(bestScore, score)
                alpha = max( alpha, score)
                if(beta <= alpha):
                    break
                
            i+=1
        return bestScore
    
    else:
        bestScore = float('inf')
        i = 1
        while(i<=len(BoardSpot)):
            if(BoardSpot[i] == "-"):
                BoardSpot[i] = opponentPiece
                score = miniMax(BoardSpot,depth-1,True,alpha,beta,playerPiece)
                BoardSpot[i] = "-"
                bestScore = min(bestScore, score)
                beta = min( beta, score)
                
                if beta <= alpha:
                    break
            i+=1
        return bestScore

def main():
    global Simulate
    global startTime
    sys.setrecursionlimit(3000)
    Simulate = 1
    startTime = time.time()
    gameStart()
    
if __name__ == '__main__':
    main()
import random
import ast
BoardSpot = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
Player = 0
TurnCount = 0
BoardSize = 3
Simulations = 2

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
            playerPiece = 'o'
            cpuTurn(playerPiece,Player)
        elif(Player > 1):
            Player = 0
            playerPiece = 'x'
            playTurn(playerPiece)
        
def endGame(win):
    print("Winner is ", win)
    
def cpuMakesMove(bestMove):
    global TurnCount
    BoardSpot[bestMove] = 'o'
    TurnCount+=1
    checkWin()
    
def simulationBoard(board):
    simBoard = {1 : "-",2 : "-",3 : "-",4 : "-",5 : "-",6 : "-",7 : "-",8 : "-",9 : "-",}
    i = 1
    while i<=len(board):
        simBoard[i] = board[i]
        i+=1
    return simBoard

def getMoves(board,player):
    if(player == 0):
        playerPiece = 'x'
    else:
        playerPiece = 'o'
    movesLeft = []
    i = 1
    
    while i <= len(board):
        if board[i] == '-':
            simBoard = simulationBoard(board)
            
            board[i] = playerPiece
            movesLeft.append(simBoard)
        i+=1
    return movesLeft

def cpuTurn(playerPiece, player):
    global BoardSize
    global Simulations
    evals = {}
    
    for x in range(Simulations):
        simBoard = simulationBoard(BoardSpot)
        simulatedMoves = []
        moves = getMoves(simBoard,player)

        score = BoardSize*BoardSize
        
        while(moves != []):
            attempt = random.randint(1,len(moves))-1
            simBoard = moves[attempt]
            
            simulatedMoves.append(simBoard)
            
            result = cpuCheckWin(simBoard)
            
            if(result == playerPiece):
                break
            
            score-=1

            if(player == 0):
                player = 1
            else:
                player = 0
                
            moves = getMoves(simBoard,player)
            
        first = simulatedMoves[0]
        
        firstKey = repr(first)
        
        result = cpuCheckWin(simBoard)
        if(player == 0 and result == 'x'):
            score *= -1
            
        if(firstKey in evals):
            evals[firstKey] += score
        else:
            evals[firstKey] = score
    bestMove = {}
    bestScore = 0
    firstTurn = True
    for move, score in evals.items():
        if firstTurn == True or score > bestScore:
            bestScore = score
            bestMove = ast.literal_eval(move)
            firstTurn = False
    print("\n",bestMove)    
    return 3

def cpuCheckWin(board):
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
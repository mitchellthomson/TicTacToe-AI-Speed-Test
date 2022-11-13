using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.UI;

public class Manager : MonoBehaviour
{

    public int whoTurn;
    public int turnCount;
    public GameObject[] turnIcons;
    public Sprite[] playIcons;
    public Button[] tictactoeSpaces;
    public GameObject winnerText;
    public int xScore;
    public int oScore;
    public Text xScoreDisplay;
    public Text oScoreDisplay;
    public bool isWin = false;
    public int[] Board;
    private int playerShape;
    private int botShape;
    public Canvas gameCanvas;
    public Canvas newCanvas;
    public Button resetButton;

    
    void Start()
    {
        xScore = 0;
        oScore = 0;
        
    }
    
    public void FreshGameX()
    {
        playerShape = 0;
        botShape = 1;
        newCanvas.gameObject.SetActive(false);
        gameCanvas.gameObject.SetActive(true);
        GameSetup();
    }
    public void FreshGameO()
    {
        playerShape = 1;
        botShape = 0;
        newCanvas.gameObject.SetActive(false);
        gameCanvas.gameObject.SetActive(true);
        GameSetup();
    }  

    void GameSetup()
    {
        whoTurn = 0;
        turnCount = 0;
        turnIcons[0].SetActive(true);
        turnIcons[1].SetActive(false);
        winnerText.SetActive(false);
        
        resetButton.gameObject.SetActive(false);
        for(int i = 0; i < tictactoeSpaces.Length; i++)
        {
            tictactoeSpaces[i].interactable = true;
            tictactoeSpaces[i].GetComponent<Image>().sprite = null;
        }
        Board = new int[9];
        
        for(int i=0; i<Board.GetLength(0);i++)
        {
            Board[i] = 4;
        }
        if(playerShape == 1)
        {
            cpuTurn();
        }
        
    }

    void endGame(int winner)
    {
        for(int i =0;i<tictactoeSpaces.Length; i++)
        {
            tictactoeSpaces[i].interactable = false;
        }
        if(winner == 0)
        {
            winnerText.GetComponent<Text>().text = "X WINS";
            winnerText.GetComponent<Text>().color = Color.blue;
            winnerText.SetActive(true);
            xScore += 1;
        }
        else if (winner == 1)
        {
            winnerText.GetComponent<Text>().text = "O WINS";
            winnerText.GetComponent<Text>().color = Color.red;
            winnerText.SetActive(true);
            oScore += 1;
        }
        else
        {
            winnerText.GetComponent<Text>().text = "TIE GAME";
            winnerText.GetComponent<Text>().color = Color.black;
            winnerText.SetActive(true);
        }
        resetButton.gameObject.SetActive(true);
        xScoreDisplay.text = (""+xScore);
        oScoreDisplay.text = (""+oScore);

    }
    void CheckWin(int turnCount)
    {
        int winner;
        //horizontal
        int sol1 = Board[0] + Board[1] + Board [2];
        int sol2 = Board[3] + Board[4] + Board [5];
        int sol3 = Board[6] + Board[7] + Board [8];

        //vertical
        int sol4 = Board[0] + Board[3] + Board [6];
        int sol5 = Board[1] + Board[4] + Board [7];
        int sol6 = Board[2] + Board[5] + Board [8];

        //diagnol
        int sol7 = Board[0] + Board[4] + Board [8];
        int sol8 = Board[2] + Board[4] + Board [6];

        var solution = new int[] {sol1, sol2 ,sol3, sol4, sol5, sol6, sol7, sol8};

        for(int i = 0; i < solution.Length; i++)
        {
            //x wins
            if(solution[i]==0)
            {
                isWin= true;
                winner = 0;
                endGame(winner);
            }
            else if (solution[i]==3)
            {
                isWin= true;
                winner = 1;
                endGame(winner);
            }
            else if (turnCount == 9 && isWin == false)
            {
                winner = 4;
                endGame(winner);
            }
        }
    }
    public int CheckWhoWon(int playerChecker)
    {
        var check = 0;
        //horizontal
        int sol1 = Board[0] + Board[1] + Board [2];
        int sol2 = Board[3] + Board[4] + Board [5];
        int sol3 = Board[6] + Board[7] + Board [8];

        //vertical
        int sol4 = Board[0] + Board[3] + Board [6];
        int sol5 = Board[1] + Board[4] + Board [7];
        int sol6 = Board[2] + Board[5] + Board [8];

        //diagnol
        int sol7 = Board[0] + Board[4] + Board [8];
        int sol8 = Board[2] + Board[4] + Board [6];

        var solution = new int[] {sol1, sol2 ,sol3, sol4, sol5, sol6, sol7, sol8};

        for(int i = 0; i < solution.Length; i++)
        {
            //x wins
            if(solution[i]==0 && playerChecker == 0)
            {
                check = 1;
                break;
            }
            else if (solution[i]==3 && playerChecker == 1)
            {
                check = 2;
                break;
            }
            else
            {
                check = 0;
            }
        }
        return check;
    }
    
    public void cpuTurn()
    {
        float bestScore = -8000f;
        int bestMove = 0;

        for(int space = 0; space < Board.Length; space++)
        {
            
            if(Board[space] == 4)
            {
                Board[space] = botShape;
                float score = Minimax(Board,0,false);
                Board[space] = 4;

                if(score > bestScore)
                {
                    bestScore = score;
                }
                print(bestMove);
                bestMove=space;
            }
        }
        TicTacToeButton(bestMove);
    }

    public float Minimax(int[] Board, int depth, bool isMaximizing)
    {
        int winCheck = CheckWhoWon(botShape);
        //tie
        if(winCheck == 0 )
        {
            return 0;
        }
        //bot wins
        if(winCheck == 1 && botShape == 0 || winCheck == 2 && botShape == 1)
        {
            return 1;
        }
        //bot loses
        if(winCheck == 1 && botShape == 1 || winCheck == 2 && botShape == 0)
        {
            return -1;
        }
        
        if(isMaximizing)
        {
            float bestScore = -8000f;
            
            for (int i = 0; i<Board.Length; i++)
            {
                if(Board[i] == 4)
                {
                    Board[i] = botShape;
                    float score = Minimax(Board, depth + 1, false);
                    Board[i] = 4;
                    if(score > bestScore)
                    {
                        bestScore = score;
                    }
                }
            }
            return bestScore;
        }

        else
        {
            float bestScore = 8000f;
            
            for (int i = 0; i<Board.Length; i++)
            {
                if(Board[i] == 4)
                {
                    Board[i] = playerShape;
                    float score = Minimax(Board, depth + 1, true);
                    Board[i] = 4;
                    if(score > bestScore)
                    {
                        bestScore = score;
                    }
                }
            }
            return bestScore;
        }
    }
    
    public void TicTacToeButton(int WhichNumber)
    {
        
        tictactoeSpaces[WhichNumber].image.sprite = playIcons[whoTurn];
        tictactoeSpaces[WhichNumber].interactable = false;
    
        turnIcons[whoTurn].SetActive(false);
        turnCount++;
        //x = 0,   O = 1
        Board[WhichNumber] = whoTurn;

        CheckWin(turnCount);

        if(whoTurn == 0)
        {
            whoTurn = 1;
        }
        else
        {
            whoTurn = 0;
        }

        turnIcons[whoTurn].SetActive(true);

        foreach(int i in Board)
        {
            //print("Spaces: " + i);
        }
        if(whoTurn == botShape)
        {
            cpuTurn();
        }
        

        
    }

    public void ResetGame()
    {
        GameSetup();
    }


}

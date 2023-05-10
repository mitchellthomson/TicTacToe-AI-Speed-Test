### running the code
Only requirements is python, and (pytest if you want to run the testing)
All the code is in the algorithms directory, each one will need to run independently as they are running different algorithms.

## My study of Planning algorithms, speed and scaling of complexity on tictactoe

The goal of this project was to analyze planning algorithms and their effectiveness in solving complex problems. With a particular interest in the game of chess, I decided to start with a simplier game like TicTacToe to reduce computational time and allow for more extensive testing.

By analyzing various planning algorithms and their performance on a simpler game, I aimed to gain a deeper understanding of the strengths and limitations of different approaches. The insights obtained from this study can be applied to more complex problems in the future.

In order to achieve the goal of analyzing planning algorithms and their speed, I chose to investigate three commonly used algorithms: Minimax, Alpha-Beta Pruning, and Monte Carlo Tree Search. To ensure a comprehensive evaluation, I implemented each algorithm with varying levels of complexity by increasing the board size to stress test each one to its limit.

I have tried to maintain this code following the principles of clean code In particular, I have focused on implementing the Single Responsibility Principle (SRP) to ensure that each function or method within the codebase has a clear and specific purpose. As well the codebase is refactored to eliminate repeated code and as well it has been updated so each script can dynamically change its complexity to the users liking instead of having multiple files of code for multiple layers of complexity.
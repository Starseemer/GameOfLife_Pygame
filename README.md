# GameOfLife_Pygame
A Simple Implemantion of John Conway's Game Of Life with pygame

## How To Install
Install pygame `pip install pygame`

Download both **Cell.py** and **GameOfLife.py**. **They should be at the same directory**

## How To Play
Go to directory that contains Cell.py and GameOfLife.py.

Run `python GameOfLife.py`

A pygame screen will appear. At the bottom right of that screen there is a black button.
Press that button to start the life.

Each cell you see in the grid is a organism. If you click on them, they come to life. If you click a living cell it **DIES**.


## Rules Of The Game
After you start the life. Each cell obeys the 4 simple rull and they are as follows;

1. If a cell has 1 or none living neigbor, it dies becaus of solidity.
2. If a cell has 4 or more living neigbor, it dies becaus of overpopulation.
3. If a cell has 2 or 3 living neigbor, it stays alive.
4. If a not living cell has a 3 living neigbor, it comes to life.
 

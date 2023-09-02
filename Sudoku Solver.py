import tkinter
import math

######################################################################Sudoku Solver
def Sudoku_Solver(SudokuGame):
    EmptyCell = FindEmptyCell(SudokuGame)
    if EmptyCell != ("No Empty Cells"): #If there is an empty cell
        for i in range (9): #For each number 1-9
            if CheckIfValid(EmptyCell,SudokuGame,(i+1)): #Check if i is a valid number
                SudokuGame[int(EmptyCell[0])][int(EmptyCell[2])] = (i+1) #Change value to of cell to i
                if Sudoku_Solver(SudokuGame):
                    return True
                SudokuGame[int(EmptyCell[0])][int(EmptyCell[2])] = 0 #Mark cell ready for backtrack
        return False
    else: #When no empty cells can be found
        for i in range(9):
            print(SudokuGame[i]) #Prints Sudoku Game row by row     

def FindEmptyCell(SudokuGame):
    for y in range (9):
        for x in range(9):
            if SudokuGame[y][x] == 0: #If Current cell does not contain a number
                Pos=(str(y)+","+str(x)) #Current y and x co-ordinates of cell
                return Pos
    return ("No Empty Cells")
            
def CheckIfValid(Pos,SudokuGame,curnum):
    Posy = int(Pos[0]) #Current y position
    Posx = int(Pos[2]) #Current x position
    for i in range (9): #For every cell in row
        if SudokuGame[Posy][i] == curnum and Posx != i: #If cell contains the number being checked
            return False #Do not change value
    for i in range (9): #For every cell in column
        if SudokuGame[i][Posx] == curnum and Posy != i: #If cell contains the number being checked
            return False #Do not change value
    Squarey = Posy // 3 #Finds y of current Sudoku square
    Squarex = Posx // 3 #Finds x of current Sudoku square
    Starty = Squarey*3 #Finds starting y
    Startx = Squarex*3 #Finds starting x
    for y in range (3): 
        for x in range (3): 
            if SudokuGame[Starty+y][Startx+x] == curnum and (Starty+y) != Posy and (Startx+x) != Posx: #Check if cell contains number being checked
                return False #Do not change value
    return True #Change value
    
#########################################################Tkinter

def SudokuUI(SudokuGame):
    
    
#########################################################Main Code
    

    
SudokuGame = [[0,0,0,2,6,0,7,0,1],
              [6,8,0,0,7,0,0,9,0],
              [1,9,0,0,0,4,5,0,0],
              [8,2,0,1,0,0,0,4,0],
              [0,0,4,6,0,2,9,0,0],
              [0,5,0,0,0,3,0,2,8],
              [0,0,9,3,0,0,0,7,4],
              [0,4,0,0,5,0,0,3,6],
              [7,0,3,0,1,8,0,0,0]] #Defining Game to be solved
tkinter.mainloop()
Sudoku_Solver(SudokuGame) #Calls solver

import tkinter

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
        root.destroy()
        SudokuUI(SudokuGame)  

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
    Starty = (Posy // 3)*3 #Floor division to find square then multiplies to find starting
    Startx = (Posx // 3)*3 #Floor division to find square then multiplies to find starting
    for y in range (3): 
        for x in range (3): 
            if SudokuGame[Starty+y][Startx+x] == curnum and (Starty+y) != Posy and (Startx+x) != Posx: #Check if cell contains number being checked
                return False #Do not change value
    return True #Change value
    
#########################################################Tkinter

class SudokuCell:
    def __init__(self, y, x,SudokuGame): #Constructor for cell class object
        self.y=y #Y co-ordinate on board
        self.x=x #X co-ordinate on board
        num=SudokuGame[y][x] #Value of the cell
        Cell = tkinter.Button(root, text = (str(num)), command = lambda:[UpdateValue(num,y,x,SudokuGame)]) #Creation of tkinter button element with ability to increase its value on click
        Cell.grid(row=y, column=x) #Place button in grid
        
def SudokuUI(SudokuGame):
    global root
    root=tkinter.Tk() 
    root.geometry("155x275+100+100") #Uses a Fixed window position
    for y in range (9):
        for x in range (9):
            SudokuCell(y,x,SudokuGame) #Call appropriate number of cells
    SolveButton = tkinter.Button(root, text = "Solve", command = lambda:[Sudoku_Solver(SudokuGame)]) #Creates button to call the solver
    SolveButton.grid(row = 9, column = 0, columnspan=9) #Places button in grid
    root.mainloop() 
    
def UpdateValue(num,y,x,SudokuGame):
    if num!=9: #Increases value by 1 if value isnt 9
        num=num+1
    else: #Only numbers 1-9 are valid so prevents numbers larger than 9
        num=0
    SudokuGame[y][x]=(num)
    root.destroy() #Destroys tkinter UI then calls new UI with updated numbers
    SudokuUI(SudokuGame)
    
#########################################################Main Code
    
SudokuGame = [[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]] #Defining Game to be solved
SudokuUI(SudokuGame)

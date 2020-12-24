import pygame

class Cell(pygame.Rect):
    def __init__(self,row,column,x,y,width,height,living):
        self.row = row
        self.column = column
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.living = living
        self.livingCellCount = 0
    def __str__(self):
        return str(self.row) + "," + str(self.column)
    def __repr__(self):
        return str(self.row) + "," + str(self.column)
    def __eq__(self,other):
        return self.getLocAsID() == other.getLocAsID()
    def getLocAsID(self):
        return str(self.row)+str(self.column)
    def kill(self):
        self.living = False
    def born(self):
        self.living = True
    def isAlive(self):
        return self.living
    def setOnClick(self):
        if(self.isAlive()):
            self.kill()
        else:
            self.born()
        return self.living
    def checkNeigborCells(self,world):
        self.livingCellCount = 0
        if(self.column-1 >= 0):
            #Left
            if(world[self.row][self.column-1].isAlive()): # 0 -1
                self.livingCellCount += 1
            if((self.row-1) >= 0):
                #Top Left
                if(world[self.row-1][self.column-1].isAlive()): # -1 -1
                    self.livingCellCount += 1
            if(self.row+1 < len(world)):
                #Bottom Left
                if(world[self.row+1][self.column-1].isAlive()): # 1 -1
                    self.livingCellCount += 1
        if(self.column+1 < len(world[self.row])):
            #Right
            if(world[self.row][self.column+1].isAlive()): # 0 1
                self.livingCellCount += 1
            if(self.row-1 >= 0):
                #Top Right
                if(world[self.row-1][self.column+1].isAlive()): # -1 1
                    self.livingCellCount += 1
            if(self.row+1 < len(world)):
                #Bottom Right
                if(world[self.row+1][self.column+1].isAlive()): # 1 1
                    self.livingCellCount += 1
        if(self.row-1 >= 0):
            #Top
            if(world[self.row-1][self.column].isAlive()): # -1 0
                self.livingCellCount += 1
        if(self.row+1 < len(world)):
            #Bottom
            if(world[self.row+1][self.column].isAlive()): # 1 0
                self.livingCellCount += 1
    def getNeigborCells(self,world):
        neigbors = []
        if(self.column-1 >= 0):
            #Left
            
            self.livingCellCount += 1
            neigbors.append(world[self.row][self.column-1])
            if((self.row-1) >= 0):
                #Top Left
                
                self.livingCellCount += 1
                neigbors.append(world[self.row-1][self.column-1])
            if(self.row+1 < len(world)):
                #Bottom Left
                
                self.livingCellCount += 1
                neigbors.append(world[self.row+1][self.column-1])
        if(self.column+1 < len(world[self.row])):
            #Right
            
            self.livingCellCount += 1
            neigbors.append(world[self.row][self.column+1])
            if(self.row-1 >= 0):
                #Top Right
                
                self.livingCellCount += 1
                neigbors.append(world[self.row-1][self.column+1])
            if(self.row+1 < len(world)):
                #Bottom Right
                self.livingCellCount += 1
                neigbors.append(world[self.row+1][self.column+1])
        if(self.row-1 >= 0):
            #Top
            self.livingCellCount += 1
            neigbors.append(world[self.row-1][self.column])
        if(self.row+1 < len(world)):
            #Bottom
            self.livingCellCount += 1
            neigbors.append(world[self.row+1][self.column])
        return neigbors
    def obeyTheRules(self):
        willDie = False
        willBorn = False
        if(self.isAlive()):
            if(self.livingCellCount <= 1):
                willDie = True
            elif(self.livingCellCount >= 4):
                willDie = True
            else:
                willDie = False
        else:
            if(self.livingCellCount == 3):
                willBorn = True
            else:
                willDie = True
        return (willDie, willBorn)
    def draw(self, screen):
        if(self.isAlive()):
            pygame.draw.rect(screen,(255,200,0),(self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(screen,(255,200,0),(self.x,self.y,self.width,self.height),1) 
    def asRect(self):
        return Rect(self.x,self.y,self.width,self.height)

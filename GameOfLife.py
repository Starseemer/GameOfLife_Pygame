
import pygame, time, sys, os

sys.path.append(".")

from Cell import Cell
from pygame.time import Clock

pygame.init()

WIDTH=int(os.popen("xdpyinfo | awk '/dimensions/{print $2}'").read().split('x')[0] if os.name=='posix' else os.popen('wmic PATH Win32_VideoController GET CurrentHorizontalResolution'))
HEIGHT=int(os.popen("xdpyinfo | awk '/dimensions/{print $2}'").read().split('x')[1] if os.name=='posix' else os.popen('wmic PATH Win32_VideoController GET CurrentVerticalResolution'))

screen = pygame.display.set_mode([WIDTH, HEIGHT])


class Button:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pushed = False
    def setOnClick(self, x, y):
        if(x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height):
            self.pushed = True
            return True
        self.pushed = False
        return False
    def draw(self):
        if(self.pushed):
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height),0)
        else:
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height),1)


world = []
for i in range(int(WIDTH/20)):
    row = []
    for j in range(int((HEIGHT-200)/20)):
        row.append(Cell(i,j,(i*20),(j*20),20,20,False))
    world.append(row)


def parseTouch(x,y):
    cell_x = int(x/20)
    cell_y = int(y/20)
    return (cell_x,cell_y)

running = True
lifeStarted = False
clicked = False
alive_cells = []
alive_cells_as_rect = []
print(WIDTH, HEIGHT)
button = Button(WIDTH-100,HEIGHT-150,90,45)
pos = (0,0)
fliped = False
while running:
    pygame.event.pump()
    willDie = []
    willBorn = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(button.setOnClick(pos[0],pos[1])):
                if(lifeStarted):
                    lifeStarted = False
                else:
                    lifeStarted = True
                    print("Life Started")
            else:
                clicked = True

    if(clicked):
        parsed = parseTouch(pos[0],pos[1])
        if(world[parsed[0]][parsed[1]].setOnClick()):
            alive_cells.append(world[parsed[0]][parsed[1]])
            for c in world[parsed[0]][parsed[1]].getNeigborCells(world):
                if(not(c.isAlive()) and (c not in alive_cells)):
                    alive_cells.append(c)
        else:
            alive_cells.remove(world[parsed[0]][parsed[1]])
            for c in world[parsed[0]][parsed[1]].getNeigborCells(world):
                if(not(c.isAlive())):
                    alive_cells.remove(c)
    
    if(lifeStarted ):
        for cell in alive_cells:
            cell.checkNeigborCells(world)
            if(cell.obeyTheRules()[0]):
                willDie.append(cell)
            if(cell.obeyTheRules()[1]):
                willBorn.append(cell)
            
        

    screen.fill((255, 255, 255))
    if(not(fliped)):
        for i in range(len(world)):
            for j in range(len(world[i])):
                world[i][j].draw(screen)
        button.draw()
        pygame.display.flip()
        fliped = False

    print(len(alive_cells))
    for c in willDie:
        c.kill()
        alive_cells.remove(c)
    print(len(alive_cells))
    for c in willBorn:
        c.born()
        if(not(c in alive_cells)):
            alive_cells.append(c)
        for inncerCell in c.getNeigborCells(world):
            if(not(inncerCell in alive_cells)):
                alive_cells.append(inncerCell)
    
    

    #pygame.display.flip()
    pygame.display.update(alive_cells)
    clicked = False
    Clock().tick(10)

    
pygame.quit()

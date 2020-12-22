
import pygame, time, sys

sys.path.append(".")

from Cell import Cell

pygame.init()

WIDTH = 900
HEIGHT = 1000

screen = pygame.display.set_mode([WIDTH, HEIGHT])


class Button:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pushed = False
    def setOnClick(self, x, y):s
        if(x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height):
            return True
        return False
    def draw(self):
        if(self.pushed):
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height),0)
            self.pushed = False
        else:
            pygame.draw.rect(screen,(0,0,0),(self.x,self.y,self.width,self.height),1)
            self.pushed = True


world = []
for i in range(int(WIDTH/20)):
    row = []
    for j in range(int(WIDTH/20)):
        row.append(Cell(i,j,(i*20),(j*20),20,20,False))
    world.append(row)

running = True
lifeStarted = False
clicked = False
button = Button(WIDTH-100,HEIGHT-50,90,45)
pos = (0,0)
lastRunTime = time.time()
while running:
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


    screen.fill((255, 255, 255))
    
    for i in range(len(world)):
        for j in range(len(world[i])):
            if(lifeStarted ):
                world[i][j].checkNeigborCells(world)
                if(world[i][j].obeyTheRules()[0]):
                    willDie.append((i,j))
                if(world[i][j].obeyTheRules()[1]):
                    willBorn.append((i,j))
            if(clicked):
                world[i][j].setOnClick(pos[0],pos[1])
            world[i][j].draw(screen)

    for c in willDie:
        world[c[0]][c[1]].kill()
    for c in willBorn:
        world[c[0]][c[1]].born()
    button.draw()
    

    pygame.display.flip()
    clicked = False
    if(lifeStarted):
        time.sleep(0.5)
    else:
        time.sleep(0.1)

    
pygame.quit()

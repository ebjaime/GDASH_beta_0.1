import pygame, sys, os, random
import numpy as np



class Blocks(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
        # self.color=color
        # self.image = pygame.Surface([width, height])
        # self.image.fill(WHITE)
        # self.image.set_colorkey(WHITE)

        # pygame.draw.rect(self.image, color, [0,0,width,height])
        self.image = pygame.image.load("platform.png").convert_alpha()
        self.rect = self.image.get_rect()

    def moveLeft(self, vel):
        self.rect.x+=-vel

    def obstacleCreate(self, Class, heightObstacle, colorObstacle):
        self.obstacle=Class(heightObstacle, colorObstacle)
        obstacleSprites.add(self.obstacle)
    def coinCreate(self, Class):
        self.coin=Class()
        coinSprites.add(self.coin)

class createObstacle(pygame.sprite.Sprite):
    def __init__(self, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.height=height
        self.image = pygame.Surface([2, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, 2, height])
        self.rect=self.image.get_rect()

    def updateO(self, block, m):
        self.rect.x=block.rect.x+m
        self.rect.y=block.rect.y-self.height
    def collide(self):
        if pygame.sprite.spritecollide(self, ballSprites, False):
            pygame.quit()
            quit()

#class PowerUps

class createCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coinPequeno.png").convert_alpha()
        self.rect = self.image.get_rect()

    def updateO(self, block, m):
        self.rect.x=block.rect.x+m
        self.rect.y=block.rect.y-100
    def collide(self):
        if pygame.sprite.spritecollide(self, ballSprites, False):
            return True


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Ball(pygame.sprite.Sprite):
    def __init__(self,width, height,radius, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        img = pygame.image.load("Cube61.png")
        # pygame.draw.rect(self.image, WHITE, [0,0,width,height])
        pygame.transform.scale(img, (width,height), self.image)
        self.rect = self.image.get_rect()

    def collide(self, spriteGroup, listHeights):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            c=pygame.sprite.spritecollide(self, spriteGroup, False)
            if (self.rect.y==c[0].rect.y-ballwh+5 or self.rect.y==c[0].rect.y-ballwh+10) and (len(c)==1 or c[0].rect.y==c[1].rect.y): #if coolision over object; and just colliding with one object or colliding with two with the same heights
                #print self.rect.y
                return True
            else:
                print ""
                print self.rect.y
                print c[0].rect.y-ballwh+5
                pygame.quit()
                quit()
        else:
            return False

    def updateP(self, velo, spriteGroup, listHeights, i=1):
        if self.collide(spriteGroup, listHeights) and i:
            velo=0
        self.rect.y+=velo




pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
font_1 = pygame.font.SysFont('Comic Sans MS', 30)
font_2 = pygame.font.SysFont('Comic Sans MS', 80)
font_3 = pygame.font.SysFont("Comic Sans MS", 55)


clock=pygame.time.Clock()

width = 800
height = 600

if len(sys.argv) == 2:
    vel=int(sys.argv[1])*5
else:
    print "A speed is needed, please inserte in such way \"python gdash_beta.py speed\" with speed -> [1,3] "
    exit()

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("GDASH")
background=Background("background2.png", [0,0])
clock = pygame.time.Clock()

#base = pygame.image.load("MakingMap2.png").convert_alpha()


BLACK = (0,0,0)
ORANGE = (255,122,122)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

blockSprites = pygame.sprite.Group()
blockS=[]
ballSprites = pygame.sprite.Group()
obstacleSprites = pygame.sprite.Group()
coinSprites = pygame.sprite.Group()

lineY= 450   #edit only
lineX= 0
lineW = width
lineH = height- lineY
block1w=300#np.random.randint(30,70)
block1h=np.random.randint(30,70)
block1h=block1h-(block1h % 5) #function .collide from pygame only works with multiples of 5, not with random intergers
block2w=300#np.random.randint(30,70)
block2h=np.random.randint(30,70)
block2h=block2h-(block2h % 5)
block3w=300#np.random.randint(30,70)
block3h=np.random.randint(30,70)
block3h=block3h-(block3h % 5)
block4w=300#np.random.randint(30,70)
block4h=np.random.randint(30,70)
block4h=block4h-(block4h % 5)
block5w=300
block5h=np.random.randint(30,70)
block5h=block5h-(block5h % 5)
ballwh=40
ballr=ballwh/2

Block1= Blocks(block1w, block1h, RED)
Block1.rect.x=800
Block1.rect.y=lineY-block1h
blockS.append(Block1)

Block4= Blocks(block4w, block4h, ORANGE)
Block4.rect.x=800
Block4.rect.y=lineY-block4h
blockS.append(Block4)

Block3= Blocks(block3w, block3h, BLUE)
Block3.rect.x=800
Block3.rect.y=lineY-block3h
blockS.append(Block3)

Block2=Blocks(block2w, block2h, GREEN)
Block2.rect.x=800
Block2.rect.y=lineY-block2h
blockS.append(Block2)

Block5=Blocks(block5w, block5h, BLUE)
Block5.rect.x=800
Block5.rect.y=lineY-90
blockS.append(Block5)


Ball = Ball(ballwh,ballwh,ballr,RED)
Ball.rect.x=50
Ball.rect.y=lineY-ballwh

##################
blockSprites.add(Block1)
blockSprites.add(Block2)
blockSprites.add(Block3)
blockSprites.add(Block4)
blockSprites.add(Block5)

ballSprites.add(Ball)
##################

blocksY=[]

for e in blockSprites:
    blocksY.append(e.rect.y-ballwh+5)


for e in list(blockSprites):
    e.obstacleCreate(createObstacle, np.random.randint(20,50), GREEN)
    e.coinCreate(createCoin)

print blocksY

movingBlocks=[0]    #only one moving at first
staticBlocks=[1,2,3,4]

nottrue=True
ascend=False
descend=False

n = 0   #index of block at the moment
m = np.random.randint(0, 300) #where to put obstacle over block
#blockS=list(blockSprites)   #CONVERT GROUP INTO LIST

jump=150
points=0

menu=0
selection=0
selected=(255,0,0)
nselected=(0,0,0)
#MAIN LOOP

while nottrue:
    # MENU

    if menu:
        display.fill([0, 0, 0])
        display.blit(background.image, background.rect)
        title = font_2.render(' GDASH v1.0 '.format(points), False, (0, 0, 0))
        author = font_3.render(' by  EBJAIME '.format(points), False, (0, 0, 0))
        if not selection:
            option_1 = font_3.render('PLAY'.format(points), False, selected)
            option_2 = font_3.render('SETTINGS'.format(points), False, nselected)
        else:
            option_1 = font_3.render('PLAY'.format(points), False, nselected)
            option_2 = font_3.render('SETTINGS'.format(points), False, selected)

        display.blit(title,(200,100))
        display.blit(author,(250,200))
        display.blit(option_1,(200,300))
        display.blit(option_2,(450, 300))
        for p in pygame.event.get():
            if p.type==pygame.QUIT:
                nottrue=False
            if p.type==pygame.KEYDOWN:
                if p.key==pygame.K_RIGHT:
                    selection=1
                if p.key==pygame.K_LEFT:
                    selection=0
                #print selection
                if p.key==pygame.K_SPACE:
                    if not selection:
                        menu=False

    #GAMEPLAY

    if not menu:
        for p in pygame.event.get():
            if p.type==pygame.QUIT:
                nottrue=False
            if p.type==pygame.KEYDOWN:
                if p.key==pygame.K_UP:
                    if not ascend and not descend:
                        ascend=True
                        posy=Ball.rect.y    #position of ball when jumping
                    elif Ball.collide(blockSprites, blocksY):
                        descend=False
                        ascend=True
                        posy=Ball.rect.y
                    else:
                        pass

            if p.type == pygame.KEYUP:  #salto indefinido
                    descend=True
                    ascend=False


        #BACKGROUND

        display.fill([0, 0, 0])
        display.blit(background.image, background.rect) # imagen de fondo
        #display.blit(base, (0,lineY))
        pygame.draw.rect(display, BLACK, [lineX, lineY, lineW, lineH])
        textsurface = font_1.render('POINTS: {}'.format(points), False, (0, 0, 0))
        display.blit(textsurface,(600,40))

        #JUMP LOOP

        if ascend:
            if Ball.rect.y>(posy-jump):
                Ball.updateP(-5, blockSprites, blocksY, 0)
            else:
                ascend=False
                descend=True
        if descend:
            if Ball.rect.y<(lineY-ballwh):
                Ball.updateP(5, blockSprites, blocksY)
            else:
                descend=False


        #BLOCK loop


        for b in movingBlocks:
            blockS[b].moveLeft(vel)

            if blockS[b].rect.x+blockS[b].width<=0:
                blockS[b].rect.x=800
                staticBlocks.append(b)
                movingBlocks.remove(b)
                blockS[b].rect.y=lineY-blockS[b].height-random.randrange(0, 100, 5)
                coinSprites.add(blockS[b].coin) #volver a la normalidad las monedas
                blockS[b].coin.updateO(blockS[b], m)

            if blockS[b].rect.x+blockS[n].width == 800:
                randomIndex = random.choice(staticBlocks)
                staticBlocks.remove(randomIndex)
                movingBlocks.append(randomIndex)
                # print blockS[b].rect.width

        #OBSTABLE loop

        for e in list(blockSprites):
            e.obstacle.updateO(e, m)
            e.obstacle.collide()

        #COIN loop

        for e in list(blockSprites):
            if e.coin.collide():
                e.coin.rect.x=810   #hasta que vuelva el bloque a x=800
                coinSprites.remove(e.coin)
                points = points+1

            elif e.coin.rect.x==810:
                continue
            else:
                e.coin.updateO(e, m)


        #REFRESH ALL SPRITE-GROUPS

        Ball.collide(blockSprites, blocksY)

        blockSprites.update()
        ballSprites.update()
        obstacleSprites.update()
        coinSprites.update()

        blockSprites.draw(display)
        ballSprites.draw(display)
        obstacleSprites.draw(display)
        coinSprites.draw(display)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
quit()

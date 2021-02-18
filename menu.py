import pygame
import sys
import os
#variables
worldx = 900
worldy = 700
fps=40
ani=4
main=True
BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
clicked = False
trueVar = True
transparent = (0, 0, 0, 0)

#setup
clock=pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy]) 
backdrop = pygame.image.load("images/image_background_sky_lightblue.png")
backdropbox = world.get_rect()
main=True
player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10






menuTitle = pygame.image.load("images/menu_screen.png")
menuTitleRect = menuTitle.get_rect()

event = pygame.event.wait()

mx, my = pygame.mouse.get_pos()

#def menu():
  #while True:

    #world.blit(menuTitle, menuTitleRect)
    #pygame.display.flip()

    #clicked = False
    #menuTitle = pygame.image.load("images/menu_title.png")
    #menuTitleRect = menuTitle.get_rect()
    #world.blit(menuTitle, menuTitleRect)


    #button_1 = pygame.Rect(0, 0, 900, 700)
    #button_2 = pygame.Rect(50, 200, 200, 50)
    #if button_1.collidepoint((mx, my)):
      #if clicked == trueVar:
        #print("button_1 clicked or something")
        
    #if button_2.collidepoint((mx, my)):
      #if click == True :
        #print("button_2 clicked or something")
        
    #clicked = False

    #for event in pygame.event.get():
      #if event.type == pygame.QUIT:
        #pygame.quit
        #sys.exit
      #if event.type == pygame.KEYDOWN:
        #if event.key == pygame.K_ESCAPE:
          #pygame.quit
          #sys.exit
      #if event.type == pygame.MOUSEBUTTONDOWN:
        #print("Game is started")
        #game_level_one()
        #button_1 = pygame.Rect(0, 0, 0, 0)
        
    

def game_level_one():
  print("level one")
  world.blit(backdrop, backdropbox)
  pygame.display.flip()


  #button_Up = pygame.Rect(486, 682, 96, 96)
  #button_2 = pygame.Rect(50, 200, 200, 50)
  #if button_Up.collidepoint((mx, my)):
    #print("button_up clicked")

  #if event.type == pygame.MOUSEBUTTONDOWN:
    #if button_Up.collidepoint((mx, my)):
      #print("button_up clicked")



#main loop
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
        if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
    world.blit(backdrop, backdropbox)
    #world.blit(menuTitle, menuTitleRect)
    player.update()
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)

    #menu()
    #objects
    class Player(pygame.sprite.Sprite):
      def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []

        img = pygame.image.load(images/image_background_sky_lightblue.png)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """

        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]
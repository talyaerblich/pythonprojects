import pygame
import random
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
size = (700, 500)#screen size is 700 by 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mine Game")
#loop game until user x's the tab
done = False
#clock is used to manage how fast screen updates
clock = pygame.time.Clock()
#--------------------------------------MAIN LOOP PROGRAM----------------------------------------------------------------------------------------------
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		screen.fill(GREEN)
		circle = pygame.draw.circle(screen, BLUE, (350,250), 30, 0) 
		circle.move(40, 60)
		#pygame.draw.rect(screen, RED, (-175, 175, 525, -525), 0)
		#pygame.draw.line(screen, BLUE, (0, 0), (700,500), 25)
		#game logic goes here
		#screen clearing code might go here
		#pygame.Surface.blit((350, 250), (0,0), None) #for bliting out screen
		#draw code here
		#update screen drawing 
		pygame.display.flip()#seems to flip the screen over and update whole screen
		pygame.display.update()#updates individual item on screen. put item in parameters
		clock.tick(60)#makes clock go for 60 seconds
pygame.quit()
exit()
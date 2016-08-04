import pygame
import random
x =350
y =250
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
x_speed = random.randint(-10, 10)
y_speed = random.randint(-10, 10)
ball_size = random.randint(20,80)
color_list =[WHITE,RED,BLACK,BLUE]
ball_color = color_list[random.randint(0, len(color_list)-1)]
iteration = 0
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mine Game")
done = False
clock = pygame.time.Clock()
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		screen.fill(GREEN)
		pygame.draw.circle(screen, ball_color, (x,y), ball_size, 0)
		x+= x_speed
		y+= y_speed
		if x >= (700-ball_size) or x <= (0+ball_size):
			x_speed *= -1
		if y >= (500-ball_size) or y <= (0+ball_size):
			y_speed *= -1
		pygame.display.flip()
		pygame.display.update()
		clock.tick(60)
		if iteration == 20:
			ball_color = color_list[random.randint(0, len(color_list)-1)]
			iteration = 0
		else:
			iteration += 1
		
pygame.quit()
exit()
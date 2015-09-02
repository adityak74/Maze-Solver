import pygame
import sys
import time
width,height=15,15
thickness=0
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
pink = ( 199,21,133)
black = (0,0,0)
screen = pygame.display.set_mode((640,480))		
occurrences = lambda arr, val: tuple((i,j) for i,x in enumerate(arr) for j,y in enumerate(x) if y == val) or ((-1,-1))
def mazedisplay(grid,ch,end):	
	pygame.init()
	screen.fill(green)
	zeroes=(occurrences(grid, 0))
	ones=(occurrences(grid, 1))	
	for x in zeroes:	
		pygame.draw.rect(screen,white,(x[1]*20,x[0]*20,width,height), thickness)
	for y in ones:
		pygame.draw.rect(screen,black,(y[1]*20,y[0]*20,width,height), thickness)
	if(ch==1 and end==-1):
		twos=(occurrences(grid, 2))
		for z in twos:			
			pygame.draw.rect(screen,red,(z[1]*20,z[0]*20,width,height), thickness)	
	elif(ch==2):
		a,b=end%10,end/10
		pygame.draw.rect(screen,red,(b*20,a*20,width,height), thickness)		
	pygame.display.flip()
	pygame.display.update()
	time.sleep(3)
def path(a,b):
	pygame.draw.rect(screen,blue,(b*20,a*20,width,height), thickness)
	pygame.display.update()
	time.sleep(1)
	pygame.draw.rect(screen,white,(b*20,a*20,width,height), thickness)
	pygame.display.update()
	pygame.display.flip()
	pygame.display.update()
def dest(a,b):
	pygame.draw.rect(screen,blue,(b*20,a*20,width,height), thickness)
	pygame.display.update()
	pygame.display.flip()
	pygame.display.update()
	time.sleep(10)
def visit(a,b):
	pygame.draw.rect(screen,pink,(b*20,a*20,width,height), thickness)
	pygame.display.update()
	pygame.display.flip()
	pygame.display.update()
def bfspath(path):
	import play
	for point in range(len(path)):
		a,b=int(path[point])/10,int(path[point])%10
		c=str(a)+str(b)
		play.playtile(c)
		pygame.draw.rect(screen,blue,(b*20,a*20,width,height), thickness)
		pygame.display.update()
		time.sleep(1)
		pygame.draw.rect(screen,white,(b*20,a*20,width,height), thickness)
		pygame.display.update()
		pygame.display.flip()
		pygame.display.update()

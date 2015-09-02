import pygame
import time
def playtile(a):
	print a
	a=str(a)
	pygame.init()
	pygame.mixer.music.load("/home/prabhat/Music/"+a+".mp3")
	pygame.mixer.music.play()
	time.sleep(1)

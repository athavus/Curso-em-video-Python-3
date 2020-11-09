import pygame
print(('=' * 12)+'MUSICPLAYER'+('=' * 12))
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
end = input('\nPara parar, aperte ENTER: ')

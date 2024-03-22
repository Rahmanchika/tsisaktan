from datetime import *
import pygame


pygame.init()

screen = pygame.display.set_mode((1400, 1050))
done = False

clock = pygame.image.load("mainclock.png")
minuteHand = pygame.image.load("rightarm.png")
secondHand = pygame.image.load("leftarm.png")

clockRect = clock.get_rect(center=(700, 525))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    seconds = datetime.now().second
    minutes = datetime.now().minute
    
    secondAngle = seconds * 6
    rotatedSecond = pygame.transform.rotate(secondHand, -secondAngle)
    minuteAngle = minutes * 6
    rotatedMinute = pygame.transform.rotate(minuteHand, -minuteAngle)

    secondRect = rotatedSecond.get_rect(center=clockRect.center)
    minuteRect = rotatedMinute.get_rect(center=clockRect.center)

    screen.fill((255, 255, 255))
    
    screen.blit(clock, clockRect)
    screen.blit(rotatedMinute, minuteRect)
    screen.blit(rotatedSecond, secondRect)

    pygame.display.flip()
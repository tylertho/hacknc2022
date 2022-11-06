import pygame
import os
import random
import time
import sys
from pygame.locals import *
from pygame import mixer

pygame.init()

window = pygame.display.set_mode((650, 400))
pygame.display.set_caption("Birds Aren't Real")

background = pygame.image.load(os.path.join("./", "skybg.jpeg"))
pinkBird = pygame.image.load(os.path.join("./", "pinkbird.png"))
yellowBird = pygame.image.load(os.path.join("./", "yellowbird.png"))
grayBird = pygame.image.load(os.path.join("./", "graybird.png"))
purpleBird = pygame.image.load(os.path.join("./", "purplebird.png"))

mixer.music.load("music.wav")
mixer.music.set_volume(5)
mixer.music.play()

CAMBRIA = pygame.font.SysFont('Cambria', 16)
clock = pygame.time.Clock()

window.blit(background, (0, 0))
score = 0

class Bird:
    def __init__(self, x, y, image, velocity):
        self.x: int = x
        self.y: int = y 
        self.image = image
        self.velocity: int = velocity

    def move(self):
        self.x -= self.velocity


def wait() -> bool:
    while True:
        for event in pygame.event.get():
            guessAndInput: tuple[bool, str] = ()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                guessAndInput = (True, 'pink')
                window.blit(background, (0, 0))
                return guessAndInput
            elif keys[pygame.K_LEFT]:
                guessAndInput = (True, 'yellow')
                window.blit(background, (0, 0))
                return guessAndInput
            elif keys[pygame.K_DOWN]:
                guessAndInput = (True, 'gray')
                window.blit(background, (0, 0))
                return guessAndInput
            else:
                if keys[pygame.K_RIGHT]:
                    guessAndInput = (True, 'purple')
                    window.blit(background, (0, 0))
                    return guessAndInput


def scoreInc() -> None:
    global score
    score += 1


def game_loop() -> None:
    run = True
    start = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        birdCount = 0
        birdDict: dict(str, int) = {
            'pink': 0,
            'yellow': 0,
            'gray': 0,
            'purple': 0
        }
        birdList: list[Bird] = []

        for _ in range(score + 1):

            if start:
                x = 700
                start = False
            y = random.randrange(0, 300)
            velocity = 6.9
            birdColor = random.choice([pinkBird, yellowBird, grayBird, purpleBird])
            currentBird = Bird(x, y, birdColor, velocity)
            window.blit(currentBird.image, (x, y))
            pygame.display.update()
            birdCount += 1
            if birdColor == pinkBird:
                birdDict['pink'] += 1
            elif birdColor == yellowBird:
                birdDict['yellow'] += 1
            elif birdColor == grayBird:
                birdDict['gray'] += 1
            else: 
                birdDict['purple'] += 1
            birdList.append(currentBird)
            print(birdDict)

        currentLevel = True
        while currentLevel:

            # move birds
            for bird in birdList:
                window.blit(background, (0, 0))
            for bird in birdList:
                bird.move()
                window.blit(bird.image, (bird.x, bird.y))
            pygame.display.update()
            clock.tick(30)
            if bird.x < -50:
                currentLevel = False

        userInput = False
        while not userInput:
            text = CAMBRIA.render('For the most common bird sighting:', True, (0, 0, 0))
            window.blit(text, (200, 100))
            pygame.display.update()
            text = CAMBRIA.render('Up key for Pink, Left for Yellow, Down for Gray, or Right for Purple', True, (0, 0, 0))
            window.blit(text, (100, 150))
            pygame.display.update()

            userInput = wait()

            if userInput[1] != max(birdDict, key= birdDict.get):
                run = False
            else:
                scoreInc()
      

game_loop()
import time

import pygame
import random


clock = pygame.time.Clock()

SCREEN_SIZE = (800, 800)
screen = pygame.display.set_mode(SCREEN_SIZE)

background = pygame.image.load("background-3.png")
background = pygame.transform.scale(background, SCREEN_SIZE)


class dancer:
    def __init__(self, sprite):
        self.dancing = False
        self.sprite = sprite

    def dance(self):
        self.sprite += 1
        if self.sprite == 8:
            self.sprite = 0
            shani.set_dancing(False)

    def get_sprite(self):
        return self.sprite

    def set_dancing(self, dance=True):
        self.dancing = dance

    def get_dancing(self):
        return self.dancing


shani = dancer(0)

# f0 = pygame.image.load("ballerina.png")
# f0 = pygame.transform.scale(f0, (200, 200))
# f1 = pygame.image.load("ballerina1.png")
# f1 = pygame.transform.scale(f1, (200, 200))
# f2 = pygame.image.load("ballerina2.png")
# f2 = pygame.transform.scale(f2, (200, 200))
# f3 = pygame.image.load("ballerina3.png")
# f3 = pygame.transform.scale(f3, (200, 200))
# f4 = pygame.image.load("ballerina4.png")
# f4 = pygame.transform.scale(f4, (200, 200))
# f5 = pygame.image.load("ballerina5.png")
# f5 = pygame.transform.scale(f5, (200, 200))
# f6 = pygame.image.load("ballerina6.png")
# f6 = pygame.transform.scale(f6, (200, 200))
# f7 = pygame.image.load("ballerina7.png")
# f7 = pygame.transform.scale(f7, (200, 200))
# f8 = pygame.image.load("ballerina8.png")
# f8 = pygame.transform.scale(f8, (200, 200))

frames = [pygame.transform.scale(pygame.image.load("ballerina{}.png".format(i)), (200, 200)) for i in range(9)]

arrowup = pygame.image.load("arrowup.png")
arrowleft = pygame.image.load("arrowleft.png")
arrowright = pygame.image.load("arrowright.png")
arrowdown = pygame.image.load("arrowdown.png")
arrowup = pygame.transform.scale(arrowup, (80, 80))
arrowleft = pygame.transform.scale(arrowleft, (80, 80))
arrowright = pygame.transform.scale(arrowright, (80, 80))
arrowdown = pygame.transform.scale(arrowdown, (80, 80))

correct_key_num = random.randint(1, 4)

if correct_key_num == 1:
    correct_key = pygame.K_LEFT
    key_image = arrowleft
if correct_key_num == 2:
    correct_key = pygame.K_UP
    key_image = arrowup
if correct_key_num == 3:
    correct_key = pygame.K_DOWN
    key_image = arrowdown
if correct_key_num == 4:
    correct_key = pygame.K_RIGHT
    key_image = arrowright

height = -20

speed = 10

counter = 0

points = 0

lives = 3

arrow = pygame.rect.Rect((correct_key_num * 150 + 100, height), (20, 20))
while True:

    if shani.get_dancing():
        counter += 1
        if counter == 3:
            shani.dance()
            counter = 0

    screen.fill((30, 30, 100))

    screen.blit(background, (0, 0))

    screen.blit(frames[shani.get_sprite()], (300, 400))

    screen.blit(key_image, (correct_key_num * 150, height))

    height += speed

    if height >= 800:
        time.sleep(0.5)
        lives -= 1
        if lives == 0:
            print("game over")
            print("total points:")
            print(points)
            pygame.quit()
        height = -20
        speed += 1
        correct_key_num = random.randint(1, 4)
    if correct_key_num == 1:
        correct_key = pygame.K_LEFT
        key_image = arrowleft
    if correct_key_num == 2:
        correct_key = pygame.K_UP
        key_image = arrowup
    if correct_key_num == 3:
        correct_key = pygame.K_DOWN
        key_image = arrowdown
    if correct_key_num == 4:
        correct_key = pygame.K_RIGHT
        key_image = arrowright
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == correct_key:
                height = -20
                speed += 1
                correct_key_num = random.randint(1, 4)
                points += 10

                shani.set_dancing(True)
            else:
                time.sleep(0.5)
                lives -= 1
                if lives == 0:
                    print("game over")
                    print("total points:")
                    print(points)
                    pygame.quit()
    if correct_key_num == 1:
        correct_key = pygame.K_LEFT
        key_image = arrowleft
    if correct_key_num == 2:
        correct_key = pygame.K_UP
        key_image = arrowup
    if correct_key_num == 3:
        correct_key = pygame.K_DOWN
        key_image = arrowdown
    if correct_key_num == 4:
        correct_key = pygame.K_RIGHT
        key_image = arrowright






    clock.tick(30)
    pygame.display.update()
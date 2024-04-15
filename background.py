import pygame


class Background:
    def __init__(self, size_):
        self.x = size_[0] / 2
        self.y = size_[1] / 2
        self.drawing_x = size_[0] / 8
        self.drawing_y = size_[1] / 8

        chair_img = pygame.image.load("pictures/chair.png")
        lamp_img = pygame.image.load("pictures/lamp.png")
        background_img = pygame.image.load("pictures/livingroom.jpg")

        self.chair = pygame.transform.scale(chair_img, [self.x + self.drawing_x * 1.5,
                                                        self.y + self.drawing_y * 1.5])
        self.lamp = pygame.transform.scale(lamp_img, [self.x + self.drawing_x * 1.2,
                                                      self.y + self.drawing_y * 2.8])
        self.background = pygame.transform.scale(background_img, [self.x * 2, self.y * 2])

    def display(self, screen_):
        screen = screen_

        screen.blit(self.background, [0, 0])
        screen.blit(self.lamp, [self.x - self.drawing_x * 0.5,
                                self.y - self.drawing_y * 4])
        screen.blit(self.chair, [self.x - self.drawing_x * 2.8,
                                 self.y - self.drawing_y * 2.3])

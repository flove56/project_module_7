import pygame
import math


class Body:
    def __init__(self, _size):
        self.size = _size
        self.x = self.size[0]
        self.drawing_x = self.x / 8
        self.y = self.size[1]
        self.drawing_y = self.y / 8
        self.fur_color = (248, 200, 135)  # Light brown
        self.eye_color = (237, 237, 0)  # (212, 235, 242)  # Light blue # dark yellow (237, 237, 0)
        # light yellow (255, 255, 161)
        self.iris_color = (255, 255, 255)  # White
        self.pupil_color = (0, 0, 0)  # Black
        self.nose_color = (255, 167, 182)  # Pink
        self.mouth_color = (0, 0, 0)  # Black
        self.leg_color = (50, 10, 0)  # Dark Brown
        self.feet_color = (100, 50, 10)

        self.left_ear = pygame.image.load("pictures/left ear.png")
        self.right_ear = pygame.image.load("pictures/right ear.png")
        self.leg = pygame.image.load("pictures/leg.png")

        self.segment_mass = 10
        self.segment_spring_constant = 10
        self.segment_friction = 0.1
        self.segment_force = 0

    def display(self, _screen):
        self.screen = _screen

        self.display_body()
        self.display_ears()
        self.display_eyes()
        self.display_mouth()
        self.display_nose()
        self.display_legs()
        self.display_tail()

    def display_body(self):
        rect_main_body = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                          self.y / 2 - (self.drawing_y * 1.95) / 2,
                          self.drawing_x * 1.5,
                          self.drawing_y * 1.95]
        pygame.draw.ellipse(self.screen, self.fur_color, rect_main_body)
        rect_lower_body = [self.x / 2 - (self.drawing_x * 1.61) / 2,
                           self.y / 2 - (self.drawing_y * 0.91) / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 1.61,
                           self.drawing_y * 0.91]
        pygame.draw.ellipse(self.screen, self.fur_color, rect_lower_body)
        rect_head = [self.x / 2 - (self.drawing_x * 1.5) / 2,
                     self.y / 2 - (self.drawing_y * 1.03) / 2 - self.drawing_y * 1.1,
                     self.drawing_x * 1.5,
                     self.drawing_y * 1.03]
        pygame.draw.ellipse(self.screen, self.fur_color, rect_head)

    def display_ears(self):
        """
        first have the rotation of left ears
        happy/normal = 18
        then the right ears
        happy/normal = 341
        :return: displays ears
        """
        left_ear_rot = pygame.transform.rotate(self.left_ear, 18)
        position_left = (self.x / 2 - self.drawing_x * 0.9,
                         self.y / 2 - self.drawing_y * 2.15)
        self.screen.blit(left_ear_rot, position_left)

        right_ear_rot = pygame.transform.rotate(self.right_ear, 341)
        position_left = (self.x / 2 + self.drawing_x * 0.12,
                         self.y / 2 - self.drawing_y * 2.15)
        self.screen.blit(right_ear_rot, position_left)

    def display_eyes(self):
        # this changes how big the eyes are, is smaller, then eyes bigger
        big = 4

        # Sclera
        left_eye = pygame.Rect(self.x / 2 - self.drawing_x * 0.45,
                               self.y / 2 - self.drawing_y * 1.3,
                               self.drawing_x / 3,
                               self.drawing_y / big)
        left_eye_surf = pygame.Surface(left_eye.size, pygame.SRCALPHA)
        pygame.draw.ellipse(left_eye_surf, self.eye_color, (0, 0, *left_eye.size))
        rotated_left_eye = pygame.transform.rotate(left_eye_surf, 350)
        self.screen.blit(rotated_left_eye, rotated_left_eye.get_rect(center=left_eye.center))

        right_eye = pygame.Rect(self.x / 2 + self.drawing_x * 0.15,
                                self.y / 2 - self.drawing_y * 1.3,
                                self.drawing_x / 3,
                                self.drawing_y / big)
        right_eye_surf = pygame.Surface(right_eye.size, pygame.SRCALPHA)
        pygame.draw.ellipse(right_eye_surf, self.eye_color, (0, 0, *right_eye.size))
        rotated_right_eye = pygame.transform.rotate(right_eye_surf, 10)
        self.screen.blit(rotated_right_eye, rotated_right_eye.get_rect(center=right_eye.center))

        # Iris
        left_iris = (self.x / 2 - self.drawing_x * 0.35,
                     self.y / 2 - self.drawing_y * 1.26,
                     self.drawing_x / (big * 1.5),
                     self.drawing_y / (big * 1.5))
        pygame.draw.ellipse(self.screen, self.iris_color, left_iris)

        right_iris = (self.x / 2 + self.drawing_x * 0.23,
                      self.y / 2 - self.drawing_y * 1.26,
                      self.drawing_x / (big * 1.5),
                      self.drawing_y / (big * 1.5))
        pygame.draw.ellipse(self.screen, self.iris_color, right_iris)

        # Pupil
        left_pupil = (self.x / 2 - self.drawing_x * 0.31,
                      self.y / 2 - self.drawing_y * 1.23,
                      self.drawing_x / (big * 2.5),
                      self.drawing_y / (big * 2.5))
        pygame.draw.ellipse(self.screen, self.pupil_color, left_pupil)

        right_pupil = (self.x / 2 + self.drawing_x * 0.25,
                       self.y / 2 - self.drawing_y * 1.23,
                       self.drawing_x / (big * 2.5),
                       self.drawing_y / (big * 2.5))
        pygame.draw.ellipse(self.screen, self.pupil_color, right_pupil)

    def display_mouth(self):
        mouth_left = (self.x / 2 - self.drawing_x / 11,
                      self.y / 2 - self.drawing_y * 1.1,
                      self.drawing_x / 8,
                      self.drawing_y / 4)
        pygame.draw.arc(self.screen, self.mouth_color, mouth_left, 4.71, 0)

        mouth_right = (self.x / 2,
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 8,
                       self.drawing_y / 4)
        pygame.draw.arc(self.screen, self.mouth_color, mouth_right, 3.14, 4.71)

    def display_nose(self):
        top_nose = (self.x / 2 - (self.drawing_x / 12),
                    self.y / 2 - self.drawing_y * 1.1,
                    self.drawing_x / 5,
                    self.drawing_y / 8)
        pygame.draw.ellipse(self.screen, self.nose_color, top_nose)
        bottom_nose = (self.x / 2 - (self.drawing_x / 20),
                       self.y / 2 - self.drawing_y * 1.1,
                       self.drawing_x / 9,
                       self.drawing_y / 6)
        pygame.draw.rect(self.screen, self.nose_color, bottom_nose, border_radius=8)

    def display_legs(self):
        # Feet in the back
        left_back_leg = (self.x / 2 - self.drawing_x * 0.8,
                         self.y / 2 + self.drawing_y * 0.55,
                         self.drawing_x * 0.6,
                         self.drawing_y * 0.5)
        pygame.draw.ellipse(self.screen, self.feet_color, left_back_leg)

        right_back_leg = (self.x / 2 + self.drawing_x * 0.2,
                          self.y / 2 + self.drawing_y * 0.55,
                          self.drawing_x * 0.6,
                          self.drawing_y * 0.5)
        pygame.draw.ellipse(self.screen, self.feet_color, right_back_leg)

        left_back_foot = (self.x / 2 - self.drawing_x * 0.68,
                          self.y / 2 + self.drawing_y * 0.7,
                          self.drawing_x * 0.3,
                          self.drawing_y * 0.4)
        pygame.draw.ellipse(self.screen, self.leg_color, left_back_foot)

        right_back_foot = (self.x / 2 + self.drawing_x * 0.38,
                           self.y / 2 + self.drawing_y * 0.7,
                           self.drawing_x * 0.3,
                           self.drawing_y * 0.4)
        pygame.draw.ellipse(self.screen, self.leg_color, right_back_foot)

        # Front legs
        position_right = (self.x / 2 + self.drawing_x * 0.2,
                          self.y / 2 - self.drawing_y * 0.5)
        position_left = (self.x / 2 - self.drawing_x * 0.5,
                         self.y / 2 - self.drawing_y * 0.5)
        resized_leg = pygame.transform.scale(self.leg, (self.drawing_x * 0.3, self.drawing_y * 1.7))
        self.screen.blit(resized_leg, position_right)
        self.screen.blit(resized_leg, position_left)

        # Feet in the front
        left_front_foot = (self.x / 2 - self.drawing_x * 0.56,
                           self.y / 2 + self.drawing_y * 0.98,
                           self.drawing_x * 0.4,
                           self.drawing_y * 0.3)
        pygame.draw.ellipse(self.screen, self.leg_color, left_front_foot)

        right_front_foot = (self.x / 2 + self.drawing_x * 0.15,
                            self.y / 2 + self.drawing_y * 0.98,
                            self.drawing_x * 0.4,
                            self.drawing_y * 0.3)
        pygame.draw.ellipse(self.screen, self.leg_color, right_front_foot)

    def display_tail(self):
        for segment in range (0,4):
            self.tail_segment_display(30, segment)

    def tail_segment_display(self, angle, seg_number):
        start_seg = (self.x/2 + self.drawing_x * 0.6 + seg_number,
                     self.y/2 + self.drawing_y * 0.8 + seg_number)
        seg_len = self.drawing_y
        x = start_seg[0] + math.cos(math.radians(angle)) * seg_len
        y = start_seg[1] + math.sin(math.radians(angle)) * seg_len

        pygame.draw.line(self.screen, self.feet_color, start_seg, (x, y), 10)

        """
        # Set the velocity by adding the force divided by the mass to it
        segment_velocity += (self.segment_force / self.segment_mass)
        # The previous angle gets the value of angle
        previous_angle = angle
        # The value of angle gets the velocity added
        angle += segment_velocity
        # the force is updated with the angle
        self.segment_force = -(angle / self.segment_spring_constant + self.segment_friction * segment_velocity)
        # The drawing angle is calculated by the difference of previous angle and angle
        drawing_angle = previous_angle - angle"""

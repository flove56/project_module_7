"""
bezier.py - Calculates a bezier curve from control points. 
https://www.pygame.org/wiki/BezierCurve

2007 Victor Blomqvist
Released to the Public Domain
"""
import pygame

gray = (100, 100, 100)
lightgray = (200, 200, 200)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
X, Y, Z = 0, 1, 2


def compute_bezier_points(vertices):
    num_points = 20  # was 30

    result = []

    # Makes all point into a variable
    b0x = vertices[0][0]
    b0y = vertices[0][1]
    b1x = vertices[1][0]
    b1y = vertices[1][1]
    b2x = vertices[2][0]
    b2y = vertices[2][1]
    b3x = vertices[3][0]
    b3y = vertices[3][1]

    # Compute polynomial coefficients from Bezier points
    ax = -b0x + 3 * b1x + -3 * b2x + b3x
    ay = -b0y + 3 * b1y + -3 * b2y + b3y

    bx = 3 * b0x + -6 * b1x + 3 * b2x
    by = 3 * b0y + -6 * b1y + 3 * b2y

    cx = -3 * b0x + 3 * b1x
    cy = -3 * b0y + 3 * b1y

    dx = b0x
    dy = b0y

    # Set up the number of steps and step size
    num_steps = num_points - 1  # arbitrary choice
    h = 1.0 / num_steps  # compute our step size

    # Compute forward differences from Bezier points and "h"
    point_x = dx
    point_y = dy

    first_fdx = ax * (h * h * h) + bx * (h * h) + cx * h
    first_fdy = ay * (h * h * h) + by * (h * h) + cy * h

    second_fdx = 6 * ax * (h * h * h) + 2 * bx * (h * h)
    second_fdy = 6 * ay * (h * h * h) + 2 * by * (h * h)

    third_fdx = 6 * ax * (h * h * h)
    third_fdy = 6 * ay * (h * h * h)

    # Compute points at each step
    result.append((int(point_x), int(point_y)))

    for i in range(num_steps):
        point_x += first_fdx
        point_y += first_fdy

        first_fdx += second_fdx
        first_fdy += second_fdy

        second_fdx += third_fdx
        second_fdy += third_fdy

        result.append((int(point_x), int(point_y)))

    return result


class Tail:
    def __init__(self, start_point_, x_, y_, drawing_x_, drawing_y_):
        self.start_point = start_point_
        self.x = x_
        self.y = y_
        self.drawing_x = drawing_x_
        self.drawing_y = drawing_y_

        self.end_point = None
        self.left_mid_point = None
        self.right_mid_point = None

        self.tail_scale = 0
        self.tail_speed = 0
        self.tail_width = 0

    def display_tail(self, screen_):
        self.screen = screen_

        # Control points that are later used to calculate the curve
        control_points = [self.start_point, self.left_mid_point, self.right_mid_point, self.end_point]

        """
        # Draw control points
        for p in control_points:
            pygame.draw.circle(self.screen, blue, (int(p[0]), int(p[1])), 4)

        
        # Draw control "lines"
        pygame.draw.lines(self.screen, lightgray, False, [(x[0], x[1]) for x in control_points])
        """

        # Draw bezier curve
        b_points = compute_bezier_points([(x[0], x[1]) for x in control_points])
        pygame.draw.lines(self.screen, pygame.Color("red"), False, b_points, self.tail_width)


    def update_tail(self, tail_speed_, tail_width_, max_scale_, end_indication_):
        if self.tail_width is not tail_width_:
            self.tail_speed = tail_speed_
        max_scale = max_scale_

        self.tail_width = tail_width_
        end_indication = end_indication_

        if self.tail_scale >= max_scale:
            self.tail_speed = -self.tail_speed
        if self.tail_scale <= -max_scale:
            self.tail_speed = -self.tail_speed
        self.tail_scale += self.tail_speed

        if end_indication == 'low':
            self.end_point = (self.x / 2 + self.drawing_x * 1.8,
                              self.y / 2 + self.drawing_y * 0.4)
            self.left_mid_point = (self.x/2 + self.drawing_x * 0.9,
                                   self.y/2 + self.drawing_y * 0.4 + self.drawing_y * self.tail_scale)
            self.right_mid_point = (self.x / 2 + self.drawing_x * 0.9,
                                    self.y / 2 + self.drawing_y * 0.4 - self.drawing_y * self.tail_scale)

        if end_indication == 'high':
            self.end_point = (self.x / 2 + self.drawing_x * 1.6,
                              self.y / 2 - self.drawing_y * 0.4 - self.drawing_y * 0.1 * self.tail_scale)
            self.left_mid_point = (self.x / 2 + self.drawing_x * 0.9,
                                   self.y / 2 + self.drawing_y * 0.4 + self.drawing_y * self.tail_scale)
            self.right_mid_point = (self.x / 2 + self.drawing_x * 0.9,
                                    self.y / 2 + self.drawing_y * 0.4 - self.drawing_y * self.tail_scale)


import random

import pygame

"""
bezier.py - Calculates a bezier curve from control points. 
https://www.pygame.org/wiki/BezierCurve

2007 Victor Blomqvist
Released to the Public Domain
"""

# Initialize the colors
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


""" Our own code starts here """


class Tail:
    def __init__(self, start_point_, x_, y_, drawing_x_, drawing_y_):
        # The point of the tail that is attached to the animal is set
        self.start_point = start_point_
        # Initialize drawing parameters
        self.x = x_
        self.y = y_
        self.drawing_x = drawing_x_
        self.drawing_y = drawing_y_

        # Initialize variables
        self.end_point = None
        self.left_mid_point = None
        self.right_mid_point = None
        self.tail_scale = 0.2
        self.tail_speed = 0.01
        self.tail_width = 3
        self.tail_end_movement = 0.3
        self.change_state = False
        self.max_scale = 0.5
        self.end_indication = None
        self.amount_of_hair = 20

        # Set the scalers for the end point of the tail for the different positions
        self.wanted_scalers_low = [1.6, -0.4, 0.8, 0.8]  # end_x, end_y, left_x, right_x
        self.wanted_scalers_high = [1.8, 0.4, 1.0, 0.9]  # end_x, end_y, left_x, right_x
        # Initialize the scalers for the start
        self.wanted_scalers = self.wanted_scalers_high
        self.scalers_now = [1.6, -0.4, 0.8, 0.8]
        # Calculate the proportions for the animations
        self.scalers_for_the_changes = []
        for position in range(len(self.wanted_scalers)):
            self.scalers_for_the_changes.append(
                abs((self.wanted_scalers_high[position] - self.wanted_scalers_low[position])) / 50)

    def display_tail(self, screen_):
        self.screen = screen_

        # Set the position of the end point of the tail
        self.end_point = (self.x / 2 + self.drawing_x * self.scalers_now[0],
                          self.y / 2 - self.drawing_y * self.scalers_now[1] -
                          self.drawing_y * self.tail_end_movement * self.tail_scale)
        # Set the position of the left middle point of the tail to create a Bézier curve
        self.left_mid_point = [self.x / 2 + self.drawing_x * self.scalers_now[2],
                               self.y / 2 + self.drawing_y * 0.4 + self.drawing_y * self.tail_scale]
        # Set the position of the right middle point of the tail to crate a Bézier curve
        self.right_mid_point = [self.x / 2 + self.drawing_x * self.scalers_now[3],
                                self.y / 2 + self.drawing_y * 0 - self.drawing_y * self.tail_scale]

        # Control points that are later used to calculate the curve
        control_points = [self.start_point, self.left_mid_point, self.right_mid_point, self.end_point]

        """
        # This is used to see the control points and create lines between these points
        # Draw control points
        for p in control_points:
            pygame.draw.circle(self.screen, blue, (int(p[0]), int(p[1])), 4)
        
        # Draw control "lines"
        pygame.draw.lines(self.screen, lightgray, False, [(x[0], x[1]) for x in control_points])
        """

        fur_color = [248, 200, 135]  # Light brown
        leg_color = [50, 10, 0]  # Dark Brown

        # Calculate the steps for the gradient in the tail
        steps = [(fur_color[0] - leg_color[0]) / (self.amount_of_hair + 1),
                 (fur_color[1] - leg_color[1]) / (self.amount_of_hair + 1),
                 (fur_color[2] - leg_color[2]) / (self.amount_of_hair + 1)]

        # Create hair strains
        for i in range(0, self.amount_of_hair):
            # Draw Bézier curve for each hair strain
            for x in range(1, 3):
                for y in range(1, 2):
                    control_points[x][y] += self.drawing_y * 0.015 * x
            # Each point of the control points is set into b_points
            b_points = compute_bezier_points([(x[0], x[1]) for x in control_points])
            # Creating a gradiant in color between the strands of hair
            r = fur_color[0] - int(steps[0] * i)
            g = fur_color[1] - int(steps[1] * i)
            b = fur_color[2] - int(steps[2] * i)
            # Draw a line for each strain
            pygame.draw.lines(self.screen, (r, g, b), False, b_points, self.tail_width)

    def update_tail(self, tail_stages, change_state_):
        # When there is a different state move the tail points to the correct positions
        if change_state_:  # This happens once
            # Set variables for the changing state
            self.old_max_scale = self.max_scale
            self.tail_speed = tail_stages['speed']
            self.change_state = change_state_
            self.max_scale = tail_stages['max_scale']
            self.end_indication = tail_stages['end_point']

            # Change the wanted scalers to the scalers corresponding of the position
            if self.end_indication == 'low':
                self.wanted_scalers = self.wanted_scalers_low
            if self.end_indication == 'high':
                self.wanted_scalers = self.wanted_scalers_high

        # Is the change state of the class is true
        if self.change_state:  # this happens multiple times
            # Adjust the speed to the state
            if self.tail_scale >= self.max_scale:
                self.tail_speed = -tail_stages['speed']
            if self.tail_scale <= -self.max_scale:
                self.tail_speed = tail_stages['speed']
            self.tail_scale += self.tail_speed

            # Adjust each scaler with its own proportions
            for scaler in range(len(self.wanted_scalers)):
                if self.scalers_now[scaler] > self.wanted_scalers[scaler]:
                    self.scalers_now[scaler] -= self.scalers_for_the_changes[scaler]
                if self.scalers_now[scaler] < self.wanted_scalers[scaler]:
                    self.scalers_now[scaler] += self.scalers_for_the_changes[scaler]
            # Change the change_state of the class when the ears are in the correct position
            if (self.max_scale >= self.tail_scale >= -self.max_scale and
                    self.wanted_scalers[1] - 0.02 >= self.scalers_now[1] >= self.wanted_scalers[1] + 0.02):
                self.change_state = False
        else:
            # Move the tail
            if self.tail_scale >= self.max_scale:
                self.tail_speed = -self.tail_speed
            if self.tail_scale <= -self.max_scale:
                self.tail_speed = -self.tail_speed
            self.tail_scale += self.tail_speed

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import Pygame
import pygame as pg

# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality. 
pg.init()

# clock function used to limit runtime speed
clock = pg.time.Clock()

# To indicate Pyame is running
running = True

# create the display surface object  
# of specific dimension..i.e(640, 480)
screen = pg.display.set_mode((640, 480))

# Set screen color to white
screen.fill((255, 255, 255))

# Common command to create rectangles using input
screen_rect = screen.get_rect()

# Function to move carts vertically 
def move_vertical(Cart):
    if Cart.direction.length() == 0:
        # Setting velocity in vertical direction as 5 pixels per second
        Cart.direction = pg.Vector2(5, 0)

# Making sure the Cart reverses direction upon reaching the end of screen
    Cart.rect.move_ip(*Cart.direction)
    if not screen_rect.contains(Cart.rect):
        Cart.direction *= -1
        Cart.rect.move_ip(Cart.direction)

# Function to move Carts horizontally
def move_horizontal(Cart):
    if Cart.direction.length() == 0:
        # etting velocity in horizontal direction as 5 pixels per second
        Cart.direction = pg.Vector2(0, 5)

# Making sure the Cart reverses direction upon reaching the end of screen
    Cart.rect.move_ip(*Cart.direction)
    if not screen_rect.contains(Cart.rect):
        Cart.direction *= -1
        Cart.rect.move_ip(Cart.direction)

# Function so that the Cart follows the direction of the mouse
# purely for demonstration
def move_to_mouse(Cart):
    pos = pg.mouse.get_pos()
    v = pg.Vector2(pos) - pg.Vector2(Cart.rect.center)
    if v.length() > 0:
        v.normalize_ip()
        # Speed of Cart is fixed to 5pps
    v *= 5
    Cart.rect.move_ip(*v)

# Class to set Cart attributes
class Cart(pg.sprite.Sprite):
    def __init__(self, color, pos, logic, *groups):
        super().__init__(*groups)
        self.image = pg.surface.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.logic = logic
        self.direction = pg.Vector2((0, 0))

    def update(self):
        self.logic(self)

# Defining 4 carts
# 2 move vertically, 1 horizontally and 1 follows the mouse.
sprites = pg.sprite.Group()
Cart(pg.color.Color('red'), ( 10,  10), move_vertical,   sprites)
Cart(pg.color.Color('yellow'),    (200, 400), move_vertical,   sprites)
Cart(pg.color.Color('cyan'), (500, 100), move_horizontal, sprites)
Cart(pg.color.Color('black'),  (100, 200), move_to_mouse,   sprites)

# To close the screen and quit
while running:

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    sprites.update()

    screen.fill((255, 255, 255))
    sprites.draw(screen)
    pg.display.update()

    clock.tick(60)
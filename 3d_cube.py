# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:45:03 2018

@author: ho
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),    #0
    (1, 1, -1),     #1
    (-1, 1, -1),    #2
    (-1, -1, -1),   #3
    (1, -1, 1),     #4
    (1, 1, 1),      #5
    (-1, -1, 1),    #6
    (-1, 1, 1)      #7
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    
    #(0,5),
    #(1,4)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            if x == 1:
                continue
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glColor3fv(colors[0])
    glVertex3fv((0,50,0))
    glVertex3fv((0,-50,0))
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    #x軸，y軸比例  display[0]/display[1]
    gluPerspective(60, (display[0]/display[1]), 0.1, 50.0) 

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 100, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(30)


main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:11:28 2022

@author: giacomobecatti
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal

def distance(p1, p2):
    dx2 = (p1[0] - p2[0]) * (p1[0] - p2[0])
    dy2 = (p1[1] - p2[1]) * (p1[1] - p2[1])
    dist2 = dx2 + dy2
    dist = np.sqrt(dist2)
    return (dist2, dist)


def deposit(N, L, radius):
    """
    Function used to deposit particles on a 2d square surface, if one the 
    particles being deposited overlaps with a particle already deposited the
    new particle is moved away
     

    Parameters
    ----------
    N : The number of particles to deposit.
    L : Length of the side of the surface where the particles are being 
        deposited.
    radius : Radius of the particle (used to check overlap).

    Returns
    -------
    com_parts : The position of every center of mass of the particles.

    """
    com_parts = np.zeros((N, 2))
    
    for i in range(1, N):
        com_i = uniform(0., L, 2)
        for j in range(i):
            dist2, dist = distance(com_i, com_parts[j])
            if dist <= 2 * radius:
                com_i[0] = com_i[0] + 2*radius
                com_i[1] = com_i[1] + 2*radius
        com_parts[i] = com_i
    return com_parts
    
def plot_com(positions, radius):
    position_x = positions[:, 0]
    position_y = positions[:, 1]
    plt.scatter(position_x, position_y, s = radius)
    plt.show()
  
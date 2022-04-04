import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal
from ase.atoms import Atoms


def distance(p1, p2):
    dx2 = (p1[0] - p2[0]) * (p1[0] - p2[0])
    dy2 = (p1[1] - p2[1]) * (p1[1] - p2[1])
    dist2 = dx2 + dy2
    dist = np.sqrt(dist2)
    return (dist2, dist)


def deposit(N, L, radius):
    com_parts = np.zeros((N, 2))
    
    for i in range(1, N):
        com_i = uniform(0., L, 2)
        for j in range(i):
            dist2, dist = distance(com_i, com_parts[j])
            if dist <= radius:
                com_i[0] = com_i[0] + dist
                com_i[1] = com_i[1] + dist
        com_parts[i] = com_i
    return com_parts
    

L = 100.
dx = L / 1000.
dy = dx

N_part = 100

com_parts = deposit(10, L, dx)




import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal
from ase.atoms import Atoms
from functions import deposit, plot_com, distance
from matplotlib.patches import Ellipse

radius = 2.
L = 50.

dx = radius / 4.
dy = dx

N_parts = 25

com_parts = deposit(N_parts, L, radius)





N_steps = 1000


positions = np.zeros((N_parts, 2, N_steps))

positions[:,:,0] = com_parts
NNeighbours = np.zeros(N_steps)
gamma = 2.
for i in range(N_steps-1):
    NN = 0
    for j in range (N_parts):
        for k in range(N_parts):
            if (k != j):
                disp = uniform(-dx, +dx, 2)
                if distance(positions[j,:,i], positions[k,:,i])[1] > 2 * radius:
                    positions[j,:,i+1] = np.mod(positions[j,:,i] + disp, L)
                elif distance(positions[j,:,i], positions[k,:,i])[1] <= 2 * radius:
                    positions[j,:,i+1] = positions[j,:,i]
                    NN += 1
                    break
                    
    NNeighbours[i] = NN
    
    if i%10 == 0:
        plt.axes()
        for l in range(N_parts):
            part = plt.Circle((positions[l,0,i], positions[l,1,i]), radius = radius)
            plt.gca().add_patch(part)
        plt.axis('scaled')
        name = "img_" + str(i)
        plt.xlim(0,L)
        plt.ylim(0,L)
        plt.savefig("/home/giacomobecatti/Documenti/UNIMI/Tesi/Nano/fig/" + name, format = "png")
        plt.close()
    




    

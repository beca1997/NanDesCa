import numpy as np
import matplotlib.pyplot as plt
from numpy.random import uniform, normal
from ase.atoms import Atoms
from functions import *

L = 100.
dx = L / 1000.
dy = dx

N_parts = 100

com_parts = deposit(N_parts, L, dx)

plot_com(com_parts)






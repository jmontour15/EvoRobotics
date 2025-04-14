# Imports
import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time
import sys

from simulation import SIMULATION

simulation = SIMULATION(directOrGUI = sys.argv[1], solutionID = sys.argv[2])
simulation.Run()
simulation.Get_Fitness()


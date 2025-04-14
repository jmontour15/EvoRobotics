import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time


from robot import ROBOT
from world import WORLD

class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            p.connect(p.DIRECT)
        else:
            p.connect(p.GUI)
        # self.physicsClient = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT(solutionID)

        # Gravity
        p.setGravity(0, 0, -9.8)

        # pyrosim.Prepare_To_Simulate()
    
    def Run(self):
        for i in range(c.sim_steps):
            # print(i) # prints time step
            if self.directOrGUI == "GUI":
                time.sleep(c.time_step)
            p.stepSimulation()
            self.robot.Sense(current_time_step = i)
            self.robot.Think()
            self.robot.Act(current_time_step = i)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
import pybullet as p
from pyrosim import pyrosim
import constants as c
import numpy as np

from motor import MOTOR
from sensor import SENSOR

class ROBOT():
    def __init__(self):
        self.motors = {}

        self.robot = p.loadURDF("body.urdf")

        # Set up sensor
        pyrosim.Prepare_To_Simulate(self.robot)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, current_time_step):
        # Sensors
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(current_time_step)
    
    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, current_time_step):
        for motor in self.motors:
            self.motors[motor].Set_Value(self.robot, current_time_step)
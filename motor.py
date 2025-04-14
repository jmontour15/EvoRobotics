import constants as c
import numpy as np
from pyrosim import pyrosim
import pybullet as p

class MOTOR():
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robot, desiredAngle):
        # Back Leg
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 30
        )
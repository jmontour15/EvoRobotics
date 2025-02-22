import constants as c
import numpy as np
from pyrosim import pyrosim
import pybullet as p

class MOTOR():
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        pass

    def Prepare_To_Act(self):
        self.amplitude = c.BackLeg_amplitude
        self.frequency = c.BackLeg_frequency
        self.offset = c.BackLeg_phaseOffset

        if self.jointName == b"Torso_BackLeg":
            self.frequency = self.frequency / 2

        # Sinusoidal values for movement
        motorValues = np.linspace(0, 2*np.pi, c.sim_steps)
        self.motorValues = self.amplitude * np.sin(self.frequency * motorValues + self.offset)

    def Set_Value(self, robot, i):
        # Back Leg
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robot,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[i],
            maxForce = 30
        )
    
    def Save_Values(self):
        np.save(f"data/{self.jointName}_MotorValues.npy", self.motorValues)
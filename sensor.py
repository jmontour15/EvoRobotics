import numpy as np
import constants as c
from pyrosim import pyrosim

class SENSOR():
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.sim_steps)
        pass

    def Get_Value(self, index):
        self.values[index] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if index == 999:
            print(self.values[index])

        pass

    def Save_Values(self):
        np.save(f"data/{self.linkName}_SensorValues.npy", self.values)
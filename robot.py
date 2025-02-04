import pybullet as p
from pyrosim import pyrosim

from motor import MOTOR
from sensor import SENSOR

class ROBOT():
    def __init__(self):
        self.sensors = {}
        self.motors = {}

        self.robotID = p.loadURDF("body.urdf")

        # Set up sensor
        pyrosim.Prepare_To_Simulate(self.robotID)
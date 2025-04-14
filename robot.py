import pybullet as p
from pyrosim import pyrosim
import constants as c
import numpy as np
import os

from motor import MOTOR
from sensor import SENSOR
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT():
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.motors = {}
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        os.system(f"del brain{solutionID}.nndf")
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
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(current_time_step)
    
    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Act(self, current_time_step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName.encode()].Set_Value(self.robot, desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()
    
    def Get_Fitness(self):
        # Maximizing Y coordinate in the negative direction
        yCoordinateOfLinkZero = -p.getLinkState(self.robot, 0)[0][0]
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        yPosition = basePosition[1]
        fitness = -yPosition
        # First create and fully write to the tmp file
        tmp_filename = f"tmp{self.solutionID}.txt"
        with open(tmp_filename, "w") as output:
            output.write(f'{fitness}')
    
        # After the file is fully written and closed, rename it
        fitness_filename = f"fitness{self.solutionID}.txt"
        # Check if the fitness file already exists and remove it if needed
        if os.path.exists(fitness_filename):
            os.remove(fitness_filename)
    
        # Now rename the tmp file to fitness file
        os.rename(tmp_filename, fitness_filename)
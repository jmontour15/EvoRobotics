import numpy as np
from pyrosim import pyrosim
import os
import random
import time
import constants as c

class SOLUTION():
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.L1_weights = np.random.rand(c.numSensorNuerons, c.numHiddenNeurons)
        self.L2_weights = np.random.rand(c.numHiddenNeurons, c.numHiddenNeurons)
        self.L3_weights = np.random.rand(c.numHiddenNeurons, c.numMotorNeurons)
        self.recurrent_weights = np.random.rand(c.numHiddenNeurons)
        self.L1_weights = self.L1_weights * 2 - 1
        self.L2_weights = self.L2_weights * 2 - 1
        self.L3_weights = self.L3_weights * 2 - 1
        # self.recurrent_weights = self.recurrent_weights * 2 - 1
    
    def Evaluate(self, run_method):
        pass
    
    def Start_Simulation(self, run_method):
        self.Create_World()
        self.Create_Robot()
        self.Create_Brain()
        os.system(f"start /B python simulate.py {run_method} {self.myID}")
    
    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"fitness{self.myID}.txt"):
            time.sleep(0.01)
        fitnessFile = open(f"fitness{self.myID}.txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()
        os.system(f"del fitness{self.myID}.txt")

    def Create_World(self):
        # Start sdf file
        pyrosim.Start_SDF("world.sdf")

        # Create box sdf
        pyrosim.Send_Cube(name="Box", pos=[-5, 5, 0.5], size=[1, 1, 1])

        pyrosim.End()
    
    def Create_Robot(self):
        # Robot body file name
        pyrosim.Start_URDF("body.urdf")

        # Torso
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        # Upper Legs
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        # Lower Legs
        pyrosim.Send_Joint(name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = [0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()
    
    def Create_Brain(self):
        # Start nndf file
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        # Sensor neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerRightLeg")

        # 1st hidden layer
        pyrosim.Send_Hidden_Neuron(name = 4)
        pyrosim.Send_Hidden_Neuron(name = 5)
        pyrosim.Send_Hidden_Neuron(name = 6)
        pyrosim.Send_Hidden_Neuron(name = 7)
        pyrosim.Send_Hidden_Neuron(name = 8)
        pyrosim.Send_Hidden_Neuron(name = 9)
        pyrosim.Send_Hidden_Neuron(name = 10)
        pyrosim.Send_Hidden_Neuron(name = 11)

        # 2nd hidden layer
        pyrosim.Send_Hidden_Neuron(name = 12)
        pyrosim.Send_Hidden_Neuron(name = 13)
        pyrosim.Send_Hidden_Neuron(name = 14)
        pyrosim.Send_Hidden_Neuron(name = 15)
        pyrosim.Send_Hidden_Neuron(name = 16)
        pyrosim.Send_Hidden_Neuron(name = 17)
        pyrosim.Send_Hidden_Neuron(name = 18)
        pyrosim.Send_Hidden_Neuron(name = 19)

        # Motor neurons
        # Upper Legs
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 22, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 23, jointName = "Torso_RightLeg")
        # Lower Legs
        pyrosim.Send_Motor_Neuron( name = 24 , jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron( name = 25 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 26, jointName = "LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 27, jointName = "RightLeg_LowerRightLeg")

        # Connect sensor neurons to hidden neurons
        for currentRow in range(c.numSensorNuerons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+4 , weight = self.L1_weights[currentRow][currentColumn] )
        
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow+4 , targetNeuronName = currentColumn+12 , weight = self.L2_weights[currentRow][currentColumn] )
        
        # Connect hidden neurons to motor neurons
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow+12 , targetNeuronName = currentColumn+20 , weight = self.L3_weights[currentRow][currentColumn] )
        
        '''
        # Connect hidden neurons to themselves (recurrent synapses)
        for currentRow in range(c.numHiddenNeurons):
            pyrosim.Send_Synapse( sourceNeuronName = currentRow+4, targetNeuronName = currentRow+4 , weight = self.recurrent_weights[currentRow])
        '''

        pyrosim.End()
        exit()
    
    def Mutate(self):
        # Randomly choose synapse layer 1, 2, or 3 to mutate
        layer = random.randint(1, 3)

        # Sensor -> hidden
        if layer == 1:
            randomRow = random.randint(0, c.numSensorNuerons-1)
            randomColumn = random.randint(0,c.numHiddenNeurons-1)
            self.L1_weights[randomRow,randomColumn] = random.random() * 2 - 1
        # Recurrent
        elif layer == 2:
            randomRow = random.randint(0, c.numHiddenNeurons-1)
            randomColumn = random.randint(0, c.numHiddenNeurons-1)
            self.L2_weights[randomRow, randomColumn] = random.random() * 2 - 1
        # Hidden -> motor
        elif layer == 3:
            randomRow = random.randint(0, c.numHiddenNeurons-1)
            randomColumn = random.randint(0,c.numMotorNeurons-1)
            self.L3_weights[randomRow,randomColumn] = random.random() * 2 - 1

        
    
    def Set_ID(self, ID):
        self.myID = ID
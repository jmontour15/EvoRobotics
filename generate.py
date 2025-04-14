import pyrosim.pyrosim as pyrosim
import numpy as np
import random

def Generate_Body():
    def Create_World():
        # Start sdf file
        pyrosim.Start_SDF("world.sdf")

        # Create box sdf
        pyrosim.Send_Cube(name="Box", pos=[-5, 5, 0.5], size=[1, 1, 1])

        pyrosim.End()

    def Create_Robot():
        # Robot body file name
        pyrosim.Start_URDF("body.urdf")

        # Physical body
        pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

        pyrosim.End()

    Create_World()
    Create_Robot()

Generate_Body()

def Generate_Brain():
    # Start nndf file
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # Sensor neurons
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    
    # Motor neurons
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    # Synapses
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1.0 )

    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 1.0 )

    for sensor_neuron in range(3):
        for motor_neuron in np.arange(3, 5, 1):
            pyrosim.Send_Synapse( sourceNeuronName = sensor_neuron , targetNeuronName = motor_neuron , weight = 2*random.random()-1 )

    pyrosim.End()

Generate_Brain()
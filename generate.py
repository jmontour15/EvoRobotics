import pyrosim.pyrosim as pyrosim

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
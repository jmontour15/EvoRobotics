# Imports
import constants as c
import numpy as np
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

from simulation import SIMULATION

'''
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Gravity
p.setGravity(0, 0, -9.8)

# Send box to simulation
p.loadSDF("world.sdf")

# Set floor
planeId = p.loadURDF("plane.urdf")


robotID = p.loadURDF("body.urdf")

# Set up sensor
pyrosim.Prepare_To_Simulate(robotID)

# Sensor value storage
backLegSensorValues = np.zeros(c.sim_steps)
frontLegSensorValues = np.zeros(c.sim_steps)


# Sinusoidal values for movement
BackLeg_targetAngles = np.linspace(0, 2*np.pi, c.sim_steps)
BackLeg_targetAngles = c.BackLeg_amplitude * np.sin(c.BackLeg_frequency * BackLeg_targetAngles + c.BackLeg_phaseOffset)

# Sinusoidal values for movement
FrontLeg_targetAngles = np.linspace(0, 2*np.pi, c.sim_steps)
FrontLeg_targetAngles = c.FrontLeg_amplitude * np.sin(c.FrontLeg_frequency * FrontLeg_targetAngles + c.FrontLeg_phaseOffset)

# np.save("data/BackLeg_targetAngles.npy", BackLeg_targetAngles)
# np.save("data/FrontLeg_targetAngles.npy", FrontLeg_targetAngles)
# exit()

# Simulation
for i in range(c.sim_steps):
    # print(i) # prints time step
    time.sleep(c.time_step)
    p.stepSimulation()

    # Sensors
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # Motors
    # Back Leg
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = b"Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = BackLeg_targetAngles[i],
        maxForce = 30
    )
    # Front Leg
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = b"Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = FrontLeg_targetAngles[i],
        maxForce = 30
    )

np.save("data/BackLeg_sensor_values.npy", backLegSensorValues)
np.save("data/FrontLeg_sensor_values.npy", frontLegSensorValues)

p.disconnect()
'''
simulation = SIMULATION()
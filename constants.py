import numpy as np

sim_steps = 1000
time_step = 1/240 # sleeps 1/240 seconds per loop

# Back leg motor controls
BackLeg_amplitude = np.pi/4
BackLeg_frequency = 10
BackLeg_phaseOffset = 0

# Front leg motor controls
FrontLeg_amplitude = np.pi/3
FrontLeg_frequency = 15
FrontLeg_phaseOffset = np.pi/6

numberOfGenerations = 10
populationSize = 10

numSensorNuerons = 4
numHiddenNeurons = 8
numMotorNeurons = 8

motorJointRange = 0.2
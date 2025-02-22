import numpy as np
from matplotlib import pyplot as plt

'''
backLegSensorValues = np.load("data/BackLeg_sensor_values.npy")
frontLegSensorValues = np.load("data/FrontLeg_sensor_values.npy")

plt.plot(backLegSensorValues, label="Back Leg", linewidth=3.5)
plt.plot(frontLegSensorValues, label="Front Leg")
plt.title("Touch Sensor Values")
plt.legend()
plt.show()
'''

BackLeg_targetAngles = np.load("data/BackLeg_targetAngles.npy")
FrontLeg_targetAngles = np.load("data/FrontLeg_targetAngles.npy")

plt.plot(BackLeg_targetAngles, label = "Back Leg")
plt.plot(FrontLeg_targetAngles, label = "Front Leg")
plt.legend()
plt.show()

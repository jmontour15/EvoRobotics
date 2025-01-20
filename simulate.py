# Imports
import pybullet as p
import time

physicsClient = p.connect(p.GUI)
time_step = 1/120 # sleeps 1/120 seconds per loop

# Send box to simulation
p.loadSDF("box.sdf")

# Iterate 1000 times
for i in range(1001):
    print(i)
    time.sleep(time_step)
    p.stepSimulation()

p.disconnect()
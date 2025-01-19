import pybullet as p
import time

physicsClient = p.connect(p.GUI)
time_step = 1/30

for i in range(1001):
    print(i)
    time.sleep(time_step)
    p.stepSimulation()

p.disconnect()
import pybullet as p

class WORLD():
    def __init__(self):
        # Generate world
        p.loadSDF("world.sdf")

        # Set floor
        self.planeId = p.loadURDF("plane.urdf")
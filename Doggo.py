import numpy as np
import time
from src.Kinematic import *
from src.config import *
from src.Servo import *
from src.release import release_motor
import matplotlib.pyplot as plt


class Doggo:
    def __init__(self, config):
        self.config = config
        self.debug = 0
        
    def debug_info_Kinematic(self):
        self.debug = 1
        
    def temp_test(self):
        update_position_one_leg_test((0, -18.4, -100), config.RF_INDEX)
        time.sleep(5)
        release_motor()


myDog = Doggo(config = Configuration())
myDog.temp_test()
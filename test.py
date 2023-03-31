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
        
    def temp_z_sweep(self, leg_index):
        start = -40
        end = -105
        while(1):
            for i in  range(start, end, -2):
                # print(i)
                update_position_one_leg_test((0, -18.4, i), leg_index)
                time.sleep(0.03)
            for i in  range(end, start, 2):
                # print(i)
                update_position_one_leg_test((0, -18.4, i), leg_index)
                time.sleep(0.03)
            # release_motor()
            
    def temp_y_sweep(self, leg_index):
        start = 80
        end = -80
        while(1):
            for i in range(start, end, -7):
                update_position_one_leg_test((0, i, -70), leg_index)
                time.sleep(0.02)
            for i in range(end, start, 7):
                update_position_one_leg_test((0, i, -70), leg_index)
                time.sleep(0.02)
        # release_motor()
        
    def temp_x_sweep(self, leg_index):
        start = 50
        end = -25
        while(1):
            for i in range(end, start, 1):
                update_position_one_leg_test((i, -18.4, -40), leg_index)
                time.sleep(0.02)
            for i in range(start, end, -1):
                update_position_one_leg_test((i, -18.4, -90), leg_index)
                time.sleep(0.02)
        # release_motor()


myDog = Doggo(config = Configuration())
myDog.temp_z_sweep(1)
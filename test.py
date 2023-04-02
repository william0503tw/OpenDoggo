import numpy as np
import time
from src.Kinematic import *
from src.config import *
from src.Servo import *
from src.release import release_motor

#### For temporaliy test, messy and hard coded

class Doggo:
    def __init__(self, config):
        self.config = config
        self.debug = 0
        
    def debug_info_Kinematic(self):
        self.debug = 1
        
    def test_z_sweep_R(self, leg_index):
        
        if ( leg_index != 0) and (leg_index != 3):
            raise ValueError(f"LEG {leg_index} not belong to right")
        
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
            
    def test_y_sweep_R(self, leg_index):
        
        if ( leg_index != 0) and (leg_index != 3):
            raise ValueError(f"LEG {leg_index} not belong to right")
        
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
        
    def test_x_sweep_R(self, leg_index):
        
        if ( leg_index != 0) and (leg_index != 3):
            raise ValueError(f"LEG {leg_index} not belong to right")
        
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
        
    def test_point(self):
        update_position_one_leg_test((0, -40, -60), 0)
        update_position_one_leg_test((0, 40, -60), 1)
        update_position_one_leg_test((0, 40, -60), 2)
        update_position_one_leg_test((0, -40, -60), 3)
        # time.sleep(10)
        # release_motor()
        
    def test_calibration(self):
        move_to_offsets_point()
        
    def test_z_sweep_L(self, leg_index):
        
        if ( leg_index != 1) and (leg_index != 2):
            raise ValueError(f"LEG {leg_index} not belong to left")
        
        
        start = -40
        end = -105
        while(1):
            for i in  range(start, end, -2):
                # print(i)
                update_position_one_leg_test((0, 18.4, i), leg_index)
                time.sleep(0.03)
            for i in  range(end, start, 2):
                # print(i)
                update_position_one_leg_test((0, 18.4, i), leg_index)
                time.sleep(0.03)
            # release_motor()


myDog = Doggo(config = Configuration())
myDog.test_z_sweep_L(2)
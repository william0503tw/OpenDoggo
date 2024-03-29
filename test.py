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
                update_position_one_leg((0, -18.4, i), leg_index)
                time.sleep(0.03)
            for i in  range(end, start, 2):
                # print(i)
                update_position_one_leg((0, -18.4, i), leg_index)
                time.sleep(0.03)
            # release_motor()
            
    def test_y_sweep_R(self, leg_index):
        
        if ( leg_index != 0) and (leg_index != 3):
            raise ValueError(f"LEG {leg_index} not belong to right")
        
        start = 80
        end = -80
        while(1):
            for i in range(start, end, -7):
                update_position_one_leg((0, i, -70), leg_index)
                time.sleep(0.02)
            for i in range(end, start, 7):
                update_position_one_leg((0, i, -70), leg_index)
                time.sleep(0.02)
        # release_motor()
        
    def test_x_sweep_R(self, leg_index):
        
        if ( leg_index != 0) and (leg_index != 3):
            raise ValueError(f"LEG {leg_index} not belong to right")
        
        start = 50
        end = -25
        while(1):
            for i in range(end, start, 1):
                update_position_one_leg((i, -18.4, -40), leg_index)
                time.sleep(0.02)
            for i in range(start, end, -1):
                update_position_one_leg((i, -18.4, -90), leg_index)
                time.sleep(0.02)
        # release_motor()
        
    def test_point(self):
        update_position_one_leg((0, -40, -60), 0)
        update_position_one_leg((0, 40, -60), 1)
        update_position_one_leg((0, 40, -60), 2)
        update_position_one_leg((0, -40, -60), 3)
        time.sleep(10)
        release_motor()
        
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
                update_position_one_leg((0, 18.4, i), leg_index)
                time.sleep(0.03)
            for i in  range(end, start, 2):
                # print(i)
                update_position_one_leg((0, 18.4, i), leg_index)
                time.sleep(0.03)
            # release_motor()
    
    def test_y_sweep_L(self, leg_index):
        if ( leg_index != 1) and (leg_index != 2):
            raise ValueError(f"LEG {leg_index} not belong to left")
        
        start = 80
        end = -80
        while(1):
            for i in range(start, end, -7):
                update_position_one_leg((0, i, -70), leg_index)
                time.sleep(0.02)
            for i in range(end, start, 7):
                update_position_one_leg((0, i, -70), leg_index)
                time.sleep(0.02)
        # release_motor()
        
    def test_x_sweep_L(self, leg_index):
        if ( leg_index != 1) and (leg_index != 2):
            raise ValueError(f"LEG {leg_index} not belong to left")
        
        start = 50
        end = -25
        speed = 5
        while(1):
            for i in range(end, start, speed):
                update_position_one_leg((i, 18.4, -40), leg_index)
                time.sleep(0.02)
            for i in range(-40, -90, -speed):
                update_position_one_leg((50, 18.4, i), leg_index)
                time.sleep(0.02)
            for i in range(start, end, -speed):
                update_position_one_leg((i, 18.4, -90), leg_index)
                time.sleep(0.02)
            for i in range(-90, -40, speed):
                update_position_one_leg((-25, 18.4, i), leg_index)
                time.sleep(0.02)
        # release_motor()
        
    def test_four_simutaneous_point(self):
        a = np.array(
            [
                [60, 60, -60, -60],
                [-88, 88, 88, -88],
                [-60, -60, -60, -60]
            ]
        )
        update_four_leg(a)
        
    def test_four_simutaneous_continuous(self):
        while(1):
            for i in range(40, 100 ,15):
                update_four_leg(np.array(
                    [
                        [60, 60, -60, -60],
                        [-55, 55, 55, -55],
                        [-i, -i, -i, -i]
                    ]
                ))
                time.sleep(0.01)
            for i in range(100, 40, -15):
                update_four_leg(np.array(
                    [
                        [60, 60, -60, -60],
                        [-55, 55, 55, -55],
                        [-i, -i, -i, -i]
                    ]
                ))
            time.sleep(0.01)

myDog = Doggo(config = Configuration())
myDog.test_four_simutaneous_continuous()
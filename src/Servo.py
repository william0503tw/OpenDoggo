# Output the angle of 12-motor
# Interface between calculation and PCA9685
# Hardware Level Driver
from adafruit_servokit import ServoKit
from src.Kinematic import *
from src.config import *
import numpy as np

kit = ServoKit(channels=16)

def rad_to_deg(rad):
    [x, y, z] = rad
    return [x * (180.0 / np.pi), y * (180.0 / np.pi), z * (180.0 / np.pi)]


def update_position_one_leg_test(xyz, leg_index):
    
    """
    xyz -> np.array(3)
    """
    
    (t, s, sh) = rad_to_deg(one_leg_IK(xyz, leg_index, Configuration(), 1))
    #print((x,y,z))
    config = Configuration()
    
    if leg_index == 0:
        pass
        # Leg index: 0 RF
        kit.servo[12].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.RF_INDEX] + t
        kit.servo[11].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.RF_INDEX] + s
        kit.servo[10].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.RF_INDEX] + sh

    elif leg_index == 1:
        # Leg index: 1 LF
        kit.servo[9].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.LF_INDEX]
        kit.servo[8].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.LF_INDEX]
        kit.servo[7].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.LF_INDEX]

    elif leg_index == 2:
        # Leg index: 2 LB
        kit.servo[6].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.LB_INDEX]
        kit.servo[5].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.LB_INDEX]
        kit.servo[4].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.LB_INDEX]

    elif leg_index == 3:
        # Leg index: 3 RB
        kit.servo[3].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.RB_INDEX]
        kit.servo[2].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.RB_INDEX]
        kit.servo[1].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.RB_INDEX]

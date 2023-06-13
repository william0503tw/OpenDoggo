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


def update_four_leg(t):   
    # input unit : coordinate (mm)
    # This function is only for move four legs simutaneous
    # output : numpy array(3,4) => coordinate (mm)
    output = np.zeros((3,4))
    output = four_leg_IK(t, Configuration())

    for i in range(4):
        update_position_one_leg(output[:,i], i)
    
    
def update_position_one_leg(xyz, leg_index):
    # Move to given xyz position, with input coordinate, output motor angle
    """
    xyz -> np.array(3) "Before IK Calculation"
    """
    (thigh, shank, shoulder) = rad_to_deg(one_leg_IK(xyz, leg_index, Configuration()))

    config = Configuration()
    
    if leg_index == 0:
        pass
        # Leg index: 0 RF
        # print(config.SERVO_OFFSET[config.SHANK_INDEX][config.RF_INDEX] + s )
        try:
            kit.servo[12].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.RF_INDEX] + thigh
            kit.servo[11].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.RF_INDEX] + shank
            kit.servo[10].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.RF_INDEX] + shoulder
        except Exception as e :
            print("Error on Leg RF: ", e)
            
        

    elif leg_index == 1:
        # Leg index: 1 LF
        try:
            kit.servo[9].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.LF_INDEX] + thigh
            kit.servo[8].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.LF_INDEX] + shank
            kit.servo[7].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.LF_INDEX] + shoulder
        except Exception as e:
            #print("Error on Leg LF: ", e)
            pass

    elif leg_index == 2:
        # Leg index: 2 LB
        try:
            kit.servo[6].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.LB_INDEX] + thigh
            kit.servo[5].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.LB_INDEX] + shank
            kit.servo[4].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.LB_INDEX] + shoulder
        except Exception as e:
            #print("Error on Leg LB: ", e)
            pass


    elif leg_index == 3:
        # Leg index: 3 RB
        # print(config.SERVO_OFFSET[config.SHANK_INDEX][config.RB_INDEX] + shank, end="\r")
        try:
            kit.servo[3].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.RB_INDEX] + thigh
            kit.servo[2].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.RB_INDEX] + shank
            kit.servo[1].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.RB_INDEX] + shoulder
        except Exception as e:
            #print("Error on Leg RB: ", e)
            pass
        
        
def move_to_offsets_point():
    config = Configuration()
    kit.servo[12].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.RF_INDEX]
    kit.servo[11].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.RF_INDEX]
    kit.servo[10].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.RF_INDEX]
    
    kit.servo[9].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.LF_INDEX]
    kit.servo[8].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.LF_INDEX]
    kit.servo[7].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.LF_INDEX]
    
    kit.servo[6].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.LB_INDEX]
    kit.servo[5].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.LB_INDEX]
    kit.servo[4].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.LB_INDEX] 
    
    kit.servo[3].angle = config.SERVO_OFFSET[config.THIGH_INDEX][config.RB_INDEX]   
    kit.servo[2].angle = config.SERVO_OFFSET[config.SHANK_INDEX][config.RB_INDEX]
    kit.servo[1].angle = config.SERVO_OFFSET[config.SHOULDER_INDEX][config.RB_INDEX]

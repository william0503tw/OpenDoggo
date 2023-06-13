# Use for configure parameter for Doggo
import numpy as np
from enum import Enum


# Leg's index
#  1 | 0
# ---|---
#  2 | 3


class Configuration:

    def __init__(self):
        ############### Robot Basic config ###############
        self.ROBOT_NAME = "OpenDoggo"
        
        # Servo angle OFFSET[3][4]
        # Column correspond to the index of LEG, and the offset to servo from top-down
        # OFFSET:
        # THIGH / 
        # SHANK / 
        # SHOULDER
        self.SERVO_OFFSET = np.array(
            [
                [100., 93, 85, 100.],
                [77., 96, 88., 78.],
                [95., 78., 100., 83.]
            ]
        )

        ################# Robot Configuration ############
        self.THIGH_L = 55
        self.SHANK_L = 53
        self.SHOULDER_OS = 18.4

        self.BODY_L = 119.4
        self.BODY_W = 96.5


        ############# Geometry ##############
        # LEG_FB => Half of the length of the robot
        # LEG_LR => Half of the width of the robot
        self.LEG_FB = self.BODY_L / 2 
        self.LEG_LR = self.BODY_W / 2

        # For feet 1 (front left) and 2 (back left), the abduction offset is positive, for the right feet,
        # the abduction offset is negative.
        self.SHOULDER_OFFSETS = np.array(
            [
                -self.SHOULDER_OS,
                self.SHOULDER_OS,
                self.SHOULDER_OS,
                -self.SHOULDER_OS,
            ]
        )

        self.LEG_ORIGIN = np.array(
            [
                [self.LEG_FB, self.LEG_FB, -self.LEG_FB, -self.LEG_FB],
                [-self.LEG_LR, self.LEG_LR, self.LEG_LR, -self.LEG_LR],
                [           0,         0,           0,              0]
            ]
        )

        ############ Simulation ############
        self.SCALE_FACTOR = 0.5





    @property
    def RF_INDEX(self):
        return 0

    @property
    def LF_INDEX(self):
        return 1

    @property
    def LB_INDEX(self):
        return 2

    @property
    def RB_INDEX(self):
        return 3

    @property
    def THIGH_INDEX(self):
        return 0

    @property
    def SHANK_INDEX(self):
        return 1

    @property
    def SHOULDER_INDEX(self):
        return 2

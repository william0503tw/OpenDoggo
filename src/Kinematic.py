# IK solver
import numpy as np
from src.config import Configuration
import os

# Leg's index
#  1 | 0
# ---|---
#  2 | 3

def rad_to_deg(rad):
    return  rad * (180.0 / np.pi)

def one_leg_IK(target_xyz, leg_index, config, debug=0):
    (x, y, z) = target_xyz
    
    #### step 1 : RF (index 0) as main calculation result
    #### step 2 : for L and R foot, flip thigh and shank angle
    #### step 3 : for B foot, flip the shoulder angle
    
    # inverse the angle (LEFT & RIGHT for shank and thigh)
    if(leg_index == config.LB_INDEX or leg_index == config.LF_INDEX):
        left_inveres = np.array([-1, -1, 1])
    else:
        left_inveres = np.array([1, 1, 1])
        
    # inverse the angle (FRONT & BACK for shoulder)
    if(leg_index == config.RB_INDEX or leg_index == config.LB_INDEX):
        back_inverse = np.array([1, 1, -1])
    else:
        back_inverse = np.array([1, 1, 1])
        
        
    
    p_distance_yz = (y ** 2 + z ** 2) ** 0.5

    # calculate the thigh-shank length project in yz plane -> L
    footLength_project_yz = (p_distance_yz ** 2 - config.SHOULDER_OS ** 2) ** 0.5

    arccos_argument = config.SHOULDER_OFFSETS[leg_index] / footLength_project_yz
    arccos_argument = np.clip(arccos_argument, -0.99, 0.99)
    gamma_1 = np.arccos(arccos_argument)
    gamma_2 = np.arctan2(z, y)

    gamma = gamma_2 + gamma_1  # output shoulder angle
    
    

    # Hip to foot distance -> S
    D_hip_foot = (footLength_project_yz ** 2 + x ** 2) ** 0.5

    # n = (D_hip_foot ** 2 - config.SHANK_L ** 2 - config.THIGH_L ** 2) / (2 * config.THIGH_L)
    # n = np.clip(n / config.SHANK_L, -0.99, 0.99)
    # theta_2 = np.arccos(n)

    alpha_1 = np.arctan(x / footLength_project_yz)
    
    a_t = (config.THIGH_L ** 2 + D_hip_foot ** 2 - config.SHANK_L ** 2) / (2 * config.THIGH_L * D_hip_foot)
    a_t = np.clip(a_t, -0.99, 0.99)
    alpha_2 = -1 * np.arccos(a_t)
    
    alpha = alpha_1 + alpha_2
    
    b_t = (config.THIGH_L ** 2 + config.SHANK_L ** 2 - D_hip_foot ** 2) / (2 * config.THIGH_L * config.SHANK_L)
    b_t = np.clip(b_t, -0.99, 0.99)
    theta = np.arccos(b_t)
     
    beta = (np.pi/2 - np.abs(alpha)) - theta
    
    if(debug):
        os.system("clear")
        print("########## DEBUG KINEMATIC ###########")
        print()
        print("LEG: ", leg_index)
        print("xyz: ", (x, y, z))
        print()
        print("------- Length -------")
        print("d: ", round(p_distance_yz, 2))
        print("L: " , round(footLength_project_yz, 2))
        print("S: " , round(D_hip_foot, 2))
        print("h: ", config.SHOULDER_OS)
        print("hu: " , round(config.THIGH_L, 2))
        print("hl: " , round(config.SHANK_L, 2))
        print("------- Angle -------")
        print("gamma_1: " , round(rad_to_deg(gamma_1), 2))
        print("gamma_2: " , round(rad_to_deg(gamma_2), 2))
        print("gamma: " , round(rad_to_deg(gamma), 2))
        print("alpha_1: " , round(rad_to_deg(alpha_1), 2))
        print("alpha_2: " , round(rad_to_deg(alpha_2), 2)) 
        print("alpha: ", round(rad_to_deg(alpha), 2))
        print("theta: " , round(rad_to_deg(theta), 2))
        print("theta1: ", round(rad_to_deg(np.pi - np.abs(alpha)), 2))
        print("beta: " , round(rad_to_deg(beta), 2))

    print("xyz: ", (x, y, z), end = "\r")
    
    return np.array(back_inverse * left_inveres * [alpha, beta, gamma])


def four_leg_IK():
    pass




    

# IK solver
import numpy as np
from src.config import Configuration

# Leg's index
#  1 | 0
# ---|---
#  2 | 3

def rad_to_deg(rad):
    return  rad * (180.0 / np.pi)

def one_leg_IK(target_xyz, leg_index, config, debug=0):
    
    (x, y, z) = target_xyz
    
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
    
    arccos_argument = (config.THIGH_L ** 2 + D_hip_foot ** 2 - config.SHANK_L ** 2) / (2 * config.THIGH_L * D_hip_foot)
    arccos_argument = np.clip(arccos_argument, -0.99, 0.99)
    alpha_2 = -1 * np.arccos(arccos_argument)
    
    alpha = alpha_1 + alpha_2
    
    arccos_argument = (config.THIGH_L ** 2 + config.SHANK_L ** 2 - D_hip_foot ** 2) / (2 * config.THIGH_L * config.SHANK_L)
    arccos_argument = np.clip(arccos_argument, -0.99, 0.99)
    theta = np.arccos(arccos_argument)
     
    beta = theta - (np.pi + alpha)
    
    if(debug == 1):
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
        print("beta" , round(rad_to_deg(beta), 2))


    return np.array([alpha, beta, gamma])


def four_leg_IK():
    pass


config = Configuration()

xyz = (12, -20, -33)
one_leg_IK(xyz, config.RB_INDEX, config=Configuration())




    
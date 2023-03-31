from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

def release_motor():
    kit.servo[1].angle = None
    kit.servo[2].angle = None
    kit.servo[3].angle = None

    kit.servo[4].angle = None
    kit.servo[5].angle = None
    kit.servo[6].angle = None

    kit.servo[7].angle = None
    kit.servo[8].angle = None
    kit.servo[9].angle = None

    kit.servo[10].angle = None
    kit.servo[11].angle = None
    kit.servo[12].angle = None
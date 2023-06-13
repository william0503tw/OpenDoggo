import time 
import smbus2
PWR_MGT_1 = 0x6B
CONFIG = 0x1A
SAMPLE_RATE = 0x19
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
ACCEL_X_HIGH = 0x3B
ACCEL_Y_HIGH = 0x3D
ACCEL_Z_HIGH = 0x3F
GYRO_X_HIGH = 0x43
GYRO_Y_HIGH = 0x45
GYRO_Z_HIGH = 0x47
TEMP_OUT_HIGH = 0x41

def MPU_initialization():
    bus.write_byte_data(Device_Address, PWR_MGT_1, 1)
    bus.write_byte_data(Device_Address, SAMPLE_RATE, 7)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

def Read_data(reg_add):
    high = bus.read_byte_data(Device_Address, reg_add)
    low = bus.read_byte_data(Device_Address, reg_add+1)
    value = (high<<8)|low
    
    if value>35768:
        value = value-65536
    
    return value

# 1 means /dev/i2c-1
bus = smbus2.SMBus(1)

# mpu6050 address
Device_Address = 0x68
MPU_initialization()

while 1:

    ACCEL_X = Read_data(ACCEL_X_HIGH)
    ACCEL_Y = Read_data(ACCEL_Y_HIGH)
    ACCEL_Z = Read_data(ACCEL_Z_HIGH)
    GYRO_X = Read_data(GYRO_X_HIGH)
    GYRO_Y = Read_data(GYRO_Y_HIGH)
    GYRO_Z = Read_data(GYRO_Z_HIGH)
    TEMP = Read_data(TEMP_OUT_HIGH)

    Ax = ACCEL_X/16384.0
    Ay = ACCEL_Y/16384.0
    Az = ACCEL_Z/16384.0

    Gx = GYRO_X/131.0
    Gy = GYRO_Y/131.0
    Gz = GYRO_Z/131.0

    T = (TEMP/340)+36.53

    print("Acceleraton: X=%.2fg\t\t" %Ax, "Y=%.2fg\t" %Ay, "Z=%.2fg" %Az)
    print("Gs Rotation: Gx=%.2f\xb0/s\t" %Gx, "Gy=%.2f\xb0/s\t" %Gy, "Gz=%.2f\xb0/s" %Gz) 
    print("Temperature: %.2f\xb0C" %T, "\n")

    time.sleep(0.1)
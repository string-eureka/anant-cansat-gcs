#import sys
import time
import random

file = "backup.txt"

TEAM_ID=100
TIME=PACKET_COUNT=0

def write_to_file(TEAM_ID,TIME,PACKET_COUNT,ALTITUDE,TEMP,VOLTAGE,GNSS_SATS,ACCEL_X,ACCEL_Y,ACCEL_Z,GYRO_X,GYRO_Y,GYRO_Z):
    with open(file, "a") as f:
        f.write(f"{TEAM_ID},{TIME},{PACKET_COUNT},{ALTITUDE},{TEMP},{VOLTAGE},{GNSS_SATS},{ACCEL_X},{ACCEL_Y},{ACCEL_Z},{GYRO_X},{GYRO_Y},{GYRO_Z}\n")

while True:
    TIME+=1
    PACKET_COUNT+=1
    ALTITUDE,TEMP,VOLTAGE,GNSS_SATS,ACCEL_X,ACCEL_Y,ACCEL_Z,GYRO_X,GYRO_Y,GYRO_Z = [random.uniform(1,100) for _ in range(10)]

    time.sleep(1)
    write_to_file(TEAM_ID,TIME,PACKET_COUNT,ALTITUDE,TEMP,VOLTAGE,GNSS_SATS,ACCEL_X,ACCEL_Y,ACCEL_Z,GYRO_X,GYRO_Y,GYRO_Z)

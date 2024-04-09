import time
import random

file = "backup.csv"

T_SEC=T_MIN=T_HOUR=PKT_CNT=0
TEAM_ID = '026'
CUR_STATE = 'Touchdown'

def write_to_file(TEAM_ID, PKT_CNT, T_HOUR, T_MIN, T_SEC, 
    GAS_ALT, CUR_STATE, ESP_TIME, IACC_Z, 
    GPS_STATUS, GPS_LAT, GPS_LNG, 
    GPS_HR, GPS_MIN, GPS_SEC, 
    IACC_X, IACC_Y, IMAG_X, IMAG_Y, IMAG_Z, 
    GAS_PRS, GAS_TEMP, GPS_ALT, CHECKSUM):

    with open(file, "a") as f:
        f.write(f"{TEAM_ID}, {PKT_CNT}, {T_HOUR}, {T_MIN}, {T_SEC}, {GAS_ALT}, {CUR_STATE}, {ESP_TIME}, {IACC_Z}, {GPS_STATUS}, {GPS_LAT}, {GPS_LNG}, {GPS_HR}, {GPS_MIN}, {GPS_SEC}, {IACC_X}, {IACC_Y}, {IMAG_X}, {IMAG_Y}, {IMAG_Z}, {GAS_PRS}, {GAS_TEMP}, {GPS_ALT}, {CHECKSUM} \n")

while True:
    PKT_CNT+=1
    T_SEC += 1
    if T_SEC == 60:
        T_MIN += 1
        T_SEC = 0
    if T_MIN == 60:
        T_HOUR += 1
        T_MIN = 0
    GAS_ALT, ESP_TIME, IACC_Z, GPS_STATUS, GPS_LAT, GPS_LNG, GPS_HR, GPS_MIN, GPS_SEC, IACC_X, IACC_Y, IMAG_X, IMAG_Y, IMAG_Z, GAS_PRS, GAS_TEMP, GPS_ALT, CHECKSUM = [random.uniform(-5,20) for _ in range(18)]
    time.sleep(1)
    write_to_file(TEAM_ID, PKT_CNT, T_HOUR, T_MIN, T_SEC, GAS_ALT, CUR_STATE, ESP_TIME, IACC_Z, GPS_STATUS, GPS_LAT, GPS_LNG, GPS_HR, GPS_MIN, GPS_SEC, IACC_X, IACC_Y, IMAG_X, IMAG_Y, IMAG_Z, GAS_PRS, GAS_TEMP, GPS_ALT, CHECKSUM)

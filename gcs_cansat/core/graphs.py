"""
    TEAM_ID : Team ID
    PKT_CNT : Packet Count
    T_HOUR : Time in Hours
    T_MIN : Time in Mins
    T_SEC : Time in Secs
    GAS_ALT : GAS Altitude  
    CUR_STATE : State of the CanSAT
    ESP_TIME : ???
    IACC_Z : Inertial Acceleration Z
    GPS_STATUS : Status of GPS
    GPS_LAT : Latitude
    GPS_LNG : Longitude
    GPS_HR
    GPS_MIN
    GPS_SEC
    IACC_X : Inertial Acceleration X
    IACC_Y : Inertial Acceleration Y
    IMAG_X : Inetial Magnetic X
    IMAG_Y : Inetial Magnetic Y
    IMAG_Z : Inetial Magnetic Z
    GAS_PRS
    GAS_TEMP
    GPS_ALT: 
    CHECKSUM
"""

def processing():

    try:
        file = open('../backup.txt','r')
    except:
        file = open('../backup.txt','r')

    TEAM_ID, PKT_CNT, T_HOUR, T_MIN, T_SEC, GAS_ALT, CUR_STATE, ESP_TIME, IACC_Z, GPS_STATUS, GPS_LAT, GPS_LNG, GPS_HR, GPS_MIN, GPS_SEC, IACC_X, IACC_Y, IMAG_X, IMAG_Y, IMAG_Z, GAS_PRS, GAS_TEMP, GPS_ALT, CHECKSUM = [[] for _ in range (24)]  

    params = {
    "TEAM_ID" : TEAM_ID,
    "PKT_CNT": PKT_CNT,
    "T_HOUR": T_HOUR,
    "T_MIN": T_MIN,
    "T_SEC": T_SEC,
    "GAS_ALT": GAS_ALT,
    "CUR_STATE": CUR_STATE,
    "ESP_TIME": ESP_TIME,
    "IACC_Z": IACC_Z,
    "GPS_STATUS": GPS_STATUS,
    "GPS_LAT": GPS_LAT,
    "GPS_LNG": GPS_LNG,
    "GPS_HR": GPS_HR,
    "GPS_MIN": GPS_MIN,
    "GPS_SEC": GPS_SEC,
    "IACC_X": IACC_X,
    "IACC_Y": IACC_Y,
    "IMAG_X": IMAG_X,
    "IMAG_Y": IMAG_Y,
    "IMAG_Z": IMAG_Z,
    "GAS_PRS": GAS_PRS,
    "GAS_TEMP": GAS_TEMP,
    "GPS_ALT": GPS_ALT,
    "CHECKSUM": CHECKSUM,
    }

    for line in file:
        if len(line) > 1:
            values = line.split(',')
            if len(values) == 24:
                for i,j in zip(params,values):
                        try:
                            if not float(j) % 1:
                                params[i].append(int(j))
                            else:
                                params[i].append(float(j))
                        except:
                            params[i].append(j)
            else:
                for i in params:
                    try:
                        params[i].append(params[i][-1])
                    except:
                        pass   

    file.close()

    return params

def main_plot_data():

    params = processing()
    if (len(params['TEAM_ID'])):
        T_TOTAL = [params["T_HOUR"][i] * 3600 + params["T_MIN"][i] * 60 + params["T_SEC"][i] for i in range (len(params['TEAM_ID']))]
    else:
        T_TOTAL = 0

    modes = {
        "Boot": 1,
        "Launchpad": 2,
        "Test": 3,
        "Ascent": 4,
        "Deployment": 5,
        "Descent": 6,
        "Aerobrake": 7,
        "Impact": 8,
        "Touchdown": 9,
        "Unknown": 0
    }

    params["CUR_STATE"] = [modes[i.strip()] for i in params["CUR_STATE"]]

    data = {
        "PKT_CNT" : params["PKT_CNT"],
        "CUR_STATE" : params["CUR_STATE"],
        "T_TOTAL" : T_TOTAL,
        "IACC_Z" : params["IACC_Z"],
        "IACC_Y" : params["IACC_Y"],
        "IACC_X" : params["IACC_X"],
        "GAS_ALT" : params["GAS_ALT"],
        "IMAG_Z" : params["IMAG_Z"],
        "GAS_PRS" : params["GAS_PRS"],
        "GAS_TEMP" : params["GAS_TEMP"],
    }

    return data

def map_plot_data():

    params = processing()
    if (len(params['TEAM_ID'])):
        T_TOTAL = [params["T_HOUR"][i] * 3600 + params["T_MIN"][i] * 60 + params["T_SEC"][i] for i in range (len(params['TEAM_ID']))]
    else:
        T_TOTAL = 0
    data = {
        "T_TOTAL" : T_TOTAL,
        "GPS_LAT" : params["GPS_LAT"],
        "GPS_LNG" : params["GPS_LNG"],
    }

    return data 

def display_data():

    params = processing()
    try:
        T_TOTAL = ":".join([str(params["T_HOUR"][-1]), str(params["T_MIN"][-1]), str(params["T_SEC"][-1])])
    except:
        T_TOTAL = '00:00:00'

    data = {
        "TEAM_ID" : params["TEAM_ID"],
        "PKT_CNT" : params["PKT_CNT"],
        "T_TOTAL" : T_TOTAL,
        "CUR_STATE" : params["CUR_STATE"],
        "GPS_STATUS" : params["GPS_STATUS"],
    }

    return data



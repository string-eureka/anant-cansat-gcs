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
from math import pow
import gmplot

def processing():

    try:
        file = open(r'../newbackup.txt', encoding="utf8")
    except Exception as e:
        print(e)
        file = open('../backup.csv','r')

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
                # try:
                #     tl= [0,1,2,3,4,10,11,-1]
                #     for i in tl:
                #         if not float(values[i]) % 1:
                #             tvar = int(values[i])
                #         else:
                #             tvar = float(values[i])
                # except:
                #     continue
                for i,j in zip(params,values):
                        try:
                            if not float(j) % 1:
                                params[i].append(int(j))
                            else:
                                params[i].append(float(j))
                        except:
                            params[i].append(j)
            else:
                continue
                # for i in params:
                #     try:
                #         params[i].append(params[i][-1])
                #     except:
                #         pass   

    file.close()

    return params

def main_plot_data():

    params = processing()
    if (len(params['TEAM_ID'])):
        T_FIRST = params["T_HOUR"][0] * 3600 + params["T_MIN"][0] * 60 + params["T_SEC"][0]
        T_TOTAL = [params["T_HOUR"][i] * 3600 + params["T_MIN"][i] * 60 + params["T_SEC"][i] -T_FIRST + 1 for i in range (len(params['TEAM_ID']))]
        D_CURRENT = str(pow(((params["GPS_LAT"][-1]-params["GPS_LAT"][0]) ** 2) + ((params["GPS_LNG"][-1]-params["GPS_LNG"][0]) ** 2),0.5))[:6]
        GPS_LAT = [str(params["GPS_LAT"][i])[:4] for i in range(len(params['TEAM_ID']))]
        GPS_LNG = [str(params["GPS_LNG"][i])[:4] for i in range(len(params['TEAM_ID']))]
    else:
        T_TOTAL = [0]
        GPS_LAT = ["0.00"]
        GPS_LNG = ["0.00"]
        D_CURRENT = 0

    distance = [str(params["GPS_LNG"][i]) for i in range(len(params['TEAM_ID']))]
    data = {
        "T_TOTAL" : T_TOTAL,
        "PKT_CNT" : params["PKT_CNT"],
        "CUR_STATE" : params["CUR_STATE"],
        "IACC_Z" : params["IACC_Z"],
        "IACC_Y" : params["IACC_Y"],
        "IACC_X" : params["IACC_X"],
        "GAS_ALT" : params["GAS_ALT"],
        "IMAG_Z" : params["IMAG_Z"],
        "GAS_PRS" : params["GAS_PRS"],
        "GAS_TEMP" : params["GAS_TEMP"],
        "GPS_LAT" : GPS_LAT,
        "GPS_LNG" : GPS_LNG,
        "D_CURRENT" : D_CURRENT,
    }

    return data

def display_data():

    params = processing()
    print(params["T_HOUR"])
    if (len(params['TEAM_ID'])):
        T_FIRST = params["T_HOUR"][0] * 3600 + params["T_MIN"][0] * 60 + params["T_SEC"][0]
        T_TOTAL = [params["T_HOUR"][i] * 3600 + params["T_MIN"][i] * 60 + params["T_SEC"][i] - T_FIRST + 1 for i in range (len(params['TEAM_ID']))]
        D_CURRENT = str(pow(((params["GPS_LAT"][-1]-params["GPS_LAT"][0]) ** 2) + ((params["GPS_LNG"][-1]-params["GPS_LNG"][0]) ** 2),0.5))[:6]
        GPS_LAT = [str(params["GPS_LAT"][i])[:4] for i in range(len(params['TEAM_ID']))]
        GPS_LNG = [str(params["GPS_LNG"][i])[:4] for i in range(len(params['TEAM_ID']))]
    else:
        T_TOTAL = [0]
        GPS_LAT = ["0.00"]
        GPS_LNG = ["0.00"]
        D_CURRENT =  0

    # if (len(params['TEAM_ID'])):

    #     T_DISPLAY = ":".join([str(params["T_HOUR"][-1]), str(params["T_MIN"][-1]), str(params["T_SEC"][-1])])
    # else:
    #     T_DISPLAY = '00:00:00'

    data = {
        "TEAM_ID" : params["TEAM_ID"],
        "PKT_CNT" : params["PKT_CNT"],
        "T_TOTAL" : T_TOTAL,
        "CUR_STATE" : params["CUR_STATE"],
        "GPS_LAT" : GPS_LAT,
        "GPS_LNG" : GPS_LNG,
        "GPS_STATUS" : params["GPS_STATUS"],
        "D_CURRENT" : D_CURRENT,
    }

    return data

def new_map():
    
    params = processing()
    lng  = params["GPS_LAT"]
    lats = params["GPS_LNG"]
    gmap = gmplot.GoogleMapPlotter(sum(lats)/len(lats), sum(lng)/len(lng), 13)
    gmap.scatter(lats, lng, '#39FF14', size=50, marker=False)
    gmap.plot(lats, lng, 'yellow', edge_width=2.5)
    gmap.draw("core/templates/core/map.html")
    # gmap = gmplot.GoogleMapPlotter(sum(lats)/len(lats), sum(lng)/len(lng), 13)
    # gmap.scatter(lats, lng, '#39FF14', size=1, marker=False)
    # gmap.draw("/Users/aadityagoel/Downloads/IND_rds/my_map.html")

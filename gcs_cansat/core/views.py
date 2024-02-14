from django.shortcuts import render
from django.http import JsonResponse
from subprocess import call

def graphs():

    file = open('../data.txt','r')
    TEAM_ID_s, TIME_s, PACKET_COUNT_s, ALTITUDE_s, TEMP_s, VOLTAGE_s, GNSS_SATS_s, ACCEL_X_s, ACCEL_Y_s, ACCEL_Z_s, GYRO_X_s, GYRO_Y_s, GYRO_Z_s = [[] for _ in range (13)]
    
    params = {
        "TEAM_ID_s": TEAM_ID_s,
        "TIME_s": TIME_s,
        "PACKET_COUNT_s": PACKET_COUNT_s,
        "ALTITUDE_s": ALTITUDE_s,
        "TEMP_s": TEMP_s,
        "VOLTAGE_s": VOLTAGE_s,
        "GNSS_SATS_s": GNSS_SATS_s,
        "ACCEL_X_s": ACCEL_X_s,
        "ACCEL_Y_s": ACCEL_Y_s,
        "ACCEL_Z_s": ACCEL_Z_s,
        "GYRO_X_s": GYRO_X_s,
        "GYRO_Y_s": GYRO_Y_s,
        "GYRO_Z_s": GYRO_Z_s
    }

    for line in file:
        if len(line) > 1:
            values = line.split(',')
            for i,j in zip(params,values):
                    if not float(j) % 1:
                        params[i].append(int(j))
                    else:
                        params[i].append(float(j))
                    
    file.close()
    return params

def plot(request):
    context = graphs()
    exec('')
    return render(request, 'core/plot.html', context)

# call(["../main.ino;"])


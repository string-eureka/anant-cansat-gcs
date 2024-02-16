<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
document.addEventListener('DOMContentLoaded', function () {
    var altitudeCtx = document.getElementById('altitudeChart').getContext('2d');
    var altitudeChart = new Chart(altitudeCtx, {
                    type: 'line',
        options: {
            animation: {
                duration: 0
        }
    },
        data: {
            labels: {{ T_TOTAL|safe }},
            datasets: [{
                label: 'Altitude (m)',
                data: {{ GAS_ALT|safe }},
                borderColor: 'blue',
                borderWidth: 1,
                fill: false
            }]
        }
    });

    var tempCtx = document.getElementById('tempChart').getContext('2d');
    var tempChart = new Chart(tempCtx, {
                    type: 'line',
        options: {
            animation: {
                duration: 0
        }
    },
        data: {
            labels: {{ T_TOTAL|safe }},
            datasets: [{
                label: 'Temperature (C)',
                data: {{ GAS_TEMP|safe }},
                borderColor: 'green',
                borderWidth: 1,
                fill: false
            }]
        }
    });

    var accelCtx = document.getElementById('accelChart').getContext('2d');
    var accelChart = new Chart(accelCtx, {
                    type: 'line',
        options: {
            animation: {
                duration: 0
        }
    },
        data: {
            labels: {{ T_TOTAL|safe }},
            datasets: [{
                label: 'Accelerometer X',
                data: {{ IACC_X|safe }},
                borderColor: 'red',
                borderWidth: 1,
                fill: false
            },{
                label: 'Accelerometer Y',
                data: {{ IACC_Y|safe }},
                borderColor: 'blue',
                borderWidth: 1,
                fill: false
            },{
                label: 'Accelerometer Z',
                data: {{ IACC_Z|safe }},
                borderColor: 'green',
                borderWidth: 1,
                fill: false
            }]
        }
    });

    var voltageCtx = document.getElementById('voltageChart').getContext('2d');
    var voltageChart = new Chart(voltageCtx, {
                    type: 'line',
        options: {
            animation: {
                duration: 0
        }
    },
        data: {
            labels: {{ T_TOTAL|safe }},
            datasets: [{
                label: 'Voltage',
                data: {{ GAS_PRS|safe }},
                borderColor: 'purple',
                borderWidth: 1,
                fill: false
            }]
        }
    });

    var gnssCtx = document.getElementById('gnssChart').getContext('2d');
    var gnssChart = new Chart(gnssCtx, {
                    type: 'line',
        options: {
            animation: {
                duration: 0
        }
    },
        data: {
            labels: {{ T_TOTAL|safe }},
            datasets: [{
                label: 'GNSS Satellites',
                data: {{ IMAG_Z|safe }},
                borderColor: 'orange',
                borderWidth: 1,
                fill: false
            }]
        }
    });
});

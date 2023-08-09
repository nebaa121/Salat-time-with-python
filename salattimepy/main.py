import calculation
import os
import PySimpleGUI as psg
import setting
from datetime import datetime


layout = [
    [
        psg.Text(
            f"longitude: {calculation.longitude} latitude: {calculation.latitude} of the city you live in",
            key="log_lat",
        ),
        psg.Button("Change", key="-change_longitude_latitude-"),
    ],
    [
        psg.Text(f"timezone {calculation.tz(calculation.timezone)}"),
        psg.Button("Change"),
    ],
    [
        psg.Text(f"timeformat {calculation.timeformat}h"),
        psg.Button("Change", key="change_timeformat"),
    ],
    [psg.Text("Current Time: ", key="-TIME-", font=("Helvetica", 20))],
    [psg.Text(f"fajr: {calculation.times_type[0]}")],
    [psg.Text(f"Sherook: {calculation.times_type[1]}")],
    [psg.Text(f"Dohr: {calculation.times_type[2]}")],
    [psg.Text(f"Asr: {calculation.times_type[3]}")],
    [psg.Text(f"Maghreb: {calculation.times_type[4]}")],
    [psg.Text(f"Ishaa: {calculation.times_type[5]}")],
    [psg.Text(f"1st third: {calculation.times_type[6]}")],
    [psg.Text(f"Midnight: {calculation.times_type[7]}")],
    [psg.Text(f"Qiyam: {calculation.times_type[8]}")],
]


def on_setting_click():
    os.system("open ./config.ini")


window = psg.Window("salah time", layout)
while True:
    event, values = window.read(timeout=1000)

    if event == psg.WIN_CLOSED or event == "Exit":
        break

    elif event == "-change_longitude_latitude-":
        setting.latitude_and_longitude()
    elif event == "change_timeformat":
        setting.changetimeformat()
    
    current_time = datetime.now().strftime("%H:%M:%S")
    window["-TIME-"].update("Current Time: " + current_time)

window.close()

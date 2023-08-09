from configparser import ConfigParser
import PySimpleGUI as psg


config = ConfigParser()
config.read("config.ini")


def latitude_and_longitude():
    layout = [
        [
            psg.Text(
                "you can get the longitude and latitude of your city by using google or bing",
                key="warning",
            )
        ],
        [psg.Text("longitude"), psg.InputText("", key="longitude")],
        [psg.Text("latitude"), psg.InputText("", key="latitude")],
        [psg.Button("Update", key="-Update-")],
    ]
    window = psg.Window("setting", layout)
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-Update-":
            config["setting"]["longitude"] = values["longitude"]
            config["setting"]["latitude"] = values["latitude"]

            with open("config.ini", "w") as configfile:
                config.write(configfile)

            window["warning"].update("updated")
        print(event, values)
    window.close()


def changetimeformat():
    layout = [[psg.Text("", key="warner")], [psg.Button("12h"), psg.Button("24h")]]
    window = psg.Window("setting", layout)
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "Exit":
            break
        elif event == "12h":
            config["setting"]["timeformat"] = "12"
            with open("config.ini", "w") as configfile:
                config.write(configfile)
            window["warner"].update(f"format is changed to {event} restart the app")

        elif event == "24h":
            config["setting"]["timeformat"] = "24"
            with open("config.ini", "w") as configfile:
                config.write(configfile)

            window["warner"].update(f"format is changed to {event} restart the app")

    window.close()

from datetime import date
import datetime

from pyIslam.praytimes import (
    PrayerConf,
    Prayer,
    LIST_FAJR_ISHA_METHODS,
)
from pyIslam.hijri import HijriDate
from pyIslam.qiblah import Qiblah
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

longitude = float(config["setting"]["longitude"])
latitude = float(config["setting"]["latitude"])
timezone = int(config["setting"]["timezone"])
fajr_isha_method = int(config["setting"]["fajr_isha_method"])
asr_fiqh = config["setting"]["asr_fiqh"]
timeformat = int(config["setting"]["timeformat"])


pconf = PrayerConf(
    longitude,
    latitude,
    timezone,
    fajr_isha_method,
    asr_fiqh,
)

pt = Prayer(pconf, date.today())
hijri = HijriDate.today()

print("Longitude:\n\t", longitude)
print("Latitude:\n\t", latitude)


def tz(t):
    if t < 0:
        return "UTC" + str(t)
    else:
        return "UTC+" + str(t)


print("Timezone:\n\t", tz(timezone))
print(
    "Fajr and Ishaa reference:\n\t",
    LIST_FAJR_ISHA_METHODS[fajr_isha_method - 1].organizations[0],
)


# converting 24h format into 12h
def convert_to_12_hour_format(times):
    return [
        datetime.datetime.strftime(
            datetime.datetime.strptime(str(t), "%H:%M:%S"), "%I:%M %p"
        )
        for t in times
    ]


times = [
    pt.fajr_time(),
    pt.sherook_time(),
    pt.dohr_time(),
    pt.asr_time(),
    pt.maghreb_time(),
    pt.ishaa_time(),
    pt.second_third_of_night(),
    pt.midnight(),
    pt.last_third_of_night(),
]

# chacking time format from th config files
if timeformat == 12:
    times_type = convert_to_12_hour_format(times)
else:
    times_type = times


print("Asr madhab:\n\t", asr_fiqh)
print("\nPrayer times for: " + hijri.format(2) + " " + str(hijri.to_gregorian()))
print("Fajr      : " + str(times_type[0]))
print("Sherook   : " + str(times_type[1]))
print("Dohr      : " + str(times_type[2]))
print("Asr       : " + str(times_type[3]))
print("Maghreb   : " + str(times_type[4]))
print("Ishaa     : " + str(times_type[5]))
print("1st third : " + str(times_type[6]))
print("Midnight  : " + str(times_type[7]))
print("Qiyam     : " + str(times_type[8]))


print("Qiblah direction from the north: " + Qiblah(pconf).sixty())

print(times_type)

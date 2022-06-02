### Python script to show battery percentage

import psutil

## Return time in hh:mm:ss
def timeConverter(sec):
    min, sec = divmod(sec, 60)
    hr, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hr, min, sec)

battery = psutil.sensors_battery()

print("Battery percentage: ", battery.percent)
print("Power plugged in: ", battery.power_plugged)

print("Remaining Power", timeConverter(battery.secsleft))

import collections.abc
import collections
collections.MutableMapping = collections.abc.MutableMapping
from dronekit import connect ,VehicleMode , Command, LocationGlobalRelative , mavutil
from pymavlink import mavutil


vehicle = connect("tcp:127.0.0.1:5762", wait_ready=True, timeout=100)
print("bağlandı")


while True:
    
    vehicle.channels.overrides[1] = 1800

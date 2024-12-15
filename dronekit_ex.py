import collections.abc
import collections
collections.MutableMapping = collections.abc.MutableMapping
from dronekit import connect ,VehicleMode , Command, LocationGlobalRelative , mavutil

vehicle = connect("tcp:127.0.0.1:5762", wait_ready=True, timeout=100)
print("bağlandı")

def go2():
    location = LocationGlobalRelative(40.2427977, 29.0106440, 10)
    vehicle.simple_goto(location)

def mode():
    vehicle.mode = VehicleMode("GUIDED")


telemetri_verileri = {
            'altitude': vehicle.location.global_relative_frame.alt,
            'latitude': vehicle.location.global_frame.lat,
            'longitude': vehicle.location.global_frame.lon,
            'pitch': vehicle.attitude.pitch,
            'roll': vehicle.attitude.roll,
            'yaw': vehicle.attitude.yaw,
            'airspeed': vehicle.airspeed,
            'groundspeed': vehicle.groundspeed,
            'mode': vehicle.mode.name,
            'armed': vehicle.armed,
            'vertical_speed': vehicle.velocity[2],
                }

print(telemetri_verileri)

go2()
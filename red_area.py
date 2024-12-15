import collections.abc
import collections
collections.MutableMapping = collections.abc.MutableMapping
from dronekit import connect, VehicleMode,LocationGlobalRelative
import math
import time
from pymavlink import mavutil
import random

"""from sensor_msgs.msg import Image
from std_msgs.msg import Header"""

# DroneKit bağlantısı
vehicle = connect("tcp:127.0.0.1:5762")
print("baglı")

yasaklı = [[40.2330842822155,29.0052902698517],[40.2316345230103,28.9991319179535]]
konumlar = [[40.2331648,29.0112448],[40.2330656,28.99912],[40.2301664,28.9991648],[40.2302336,29.0122752]]
def mesafehesapla(lat1, lon1, lat2, lon2):
    R = 6371  
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad
    a = math.sin(delta_lat/2) * math.sin(delta_lat/2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2) * math.sin(delta_lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    mesafe = R * c*1000
    mesafe=int(mesafe)
    return mesafe


def konumagit(lat,lon,alt):
    vehicle.mode = VehicleMode("GUIDED")
    time.sleep(0.5)
    hedefkonum = LocationGlobalRelative(lat, lon, alt)
    vehicle.simple_goto(hedefkonum)

mission_count = 0
def mission():

    
    vehicle.mode="AUTO"
    time.sleep(0.5)
    yasaklı_bölge = random.choices(yasaklı)
    print(yasaklı_bölge)
    yarı_çap = 100
      
    for konum in konumlar:
        kamikazelat= konum[0]
        kamikazelon= konum[1]
        
       
        while(True):
            print(f"konum {vehicle.location.global_relative_frame.lat,vehicle.location.global_relative_frame.lon}")
            if mesafehesapla(vehicle.location.global_relative_frame.lat,vehicle.location.global_relative_frame.lon,kamikazelat,kamikazelon)<=150:
                print("konuma ulaşıldı")
                break
            if mesafehesapla(vehicle.location.global_relative_frame.lat,vehicle.location.global_relative_frame.lon,yasaklı_bölge[0][0],yasaklı_bölge[0][1])<=yarı_çap:
                vehicle.channels.overrides[1] = 1100

            time.sleep(1)
        
mission()
    

    
import urllib2
import json
import argparse
import os
import requests
import led_grid
import time
from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3

NODE_URL = "http://127.0.0.1:8000/"

def get_json(loc):
    lat,lng,alt = loc

    return json.loads(urllib2.urlopen(NODE_URL + "?lat="+str(lat) +"&lng=" + str(lng)).read())

def get_pos_by_name(location_name, apikey):
    geolocator = GoogleV3(api_key=apikey)
    loc = geolocator.geocode(location_name)
    if not loc:
        return None

    print('Your given location: %s', loc.address.encode('utf-8'))
    print('lat/long/alt: %s %s %s', loc.latitude,
             loc.longitude, loc.altitude)
    return (loc.latitude, loc.longitude, loc.altitude)

def main():
    parser = argparse.ArgumentParser()
    config_file = "config.json"

    # If config file exists, load variables from json
    load = {}
    if os.path.isfile(config_file):
        with open(config_file) as data:
            load.update(json.load(data))

    loc = get_pos_by_name(load["location"], load["google_key"])
    print loc

    while True:
        print("looping")
        forts = get_json(loc)
        print(forts)
        for fort in forts:
            if 'owned_by_team' in fort:
                
                if fort['latitude'] == 42.359092 and fort['longitude'] == -71.093987:
                    print "Alchemist Gym owned by Team " + str(fort['owned_by_team'])
                    if 'is_in_battle' in fort:
                        print "Alchemist Gym is in battle!"
                        led_grid.show_team_battle(fort['owned_by_team'])
                    else:
                        led_grid.show_team_color(fort['owned_by_team'])
        time.sleep(2)

if __name__ == '__main__':
    main()

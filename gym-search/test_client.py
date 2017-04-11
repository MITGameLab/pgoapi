import urllib2
import json
import requests
import led_grid
import time

NODE_URL = "http://127.0.0.1:8000/"

def get_json(loc):
    return json.loads(urllib2.urlopen(NODE_URL + "?loc="+str(loc)).read())

def main():
    while True:
        forts = get_json("")['data']
        print forts
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

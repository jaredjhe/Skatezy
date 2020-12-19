from radar import RadarClient
#import os
SECRET_KEY = "prj_test_pk_1384085131f3a144ad5586c9f0e906eefc2ae8e9"
radar = RadarClient(SECRET_KEY)

# Returns user's nearest ice rink addresses, given their String ip
def get_ice_rink_address(entered_ip):
  ip_location = radar.geocode.ip(entered_ip)
  user_location = (ip_location.latitude, ip_location.longitude)
  nearest_ice_rink_address = radar.search.places(near=user_location, categories="ice-skating",radius=10000)
  return nearest_ice_rink_address
def parce_rink_name(possible_rinks):
  names = [] 
  return names


#Get geofence
#nearest_ice_rink_address = get_ice_rink_address()
#geo_fence=radar.geofences.get(nearest_ice_rink_address)

#geometry = ip_location[1]
#coordinates = geometry["coordinates"]
#return coordinates[0]
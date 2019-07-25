# library to handle requests
import requests
# library for data analsysis
import pandas as pd
# library
import wikipedia as wp
import numpy as np
import folium
import json

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors


from geopy.geocoders import Nominatim

## First section of my program: Scrape, clean, organize data into dataFrame.
## Thomas Adams

# grabbed the table from wiki and saved to a df & csv
html = wp.page("List_of_postal_codes_of_Canada:_M").html().encode("UTF-8")
Toronto_FSA = pd.read_html(html)[0]
Toronto_FSA.to_csv('beautifulsoup_toronto.csv',header=0,index=False)

## First section of my program: Scrape, clean, organize data into dataFrame.
# filter out Not assigned entries
filter_tor1 = Toronto_FSA[Toronto_FSA['Borough'] != 'Not assigned'].reset_index(drop=True)

# if postcode is same for any rows. Combine the two rows with the neighborhoods separated with a comma
filter_tor2 = filter_tor1.groupby('Postcode')['Neighbourhood'].unique().agg(', '.join)
filter_tor2v = filter_tor1.groupby('Postcode')['Borough'].unique().agg(', '.join)
toronto_final = pd.concat([filter_tor2v, filter_tor2], axis=1).reset_index()







# =============================================================================
# import geocoder
# 
# def get_geocoder(postal_code):
#      # initialize your variable to None
#      lat_lng_coords = None
#      # loop until you get the coordinates
#      while(lat_lng_coords is None):
#        g = geocoder.google('{}, Toronto, Ontario'.format(postal_code))
#        lat_lng_coords = g.latlng
#      latitude = lat_lng_coords[0]
#      longitude = lat_lng_coords[1]
#      return latitude,longitude
# 
# 
# toronto_final['Latitude'], toronto_final['Longitude'] = zip(*toronto_final['Postcode'].apply(get_geocoder))  
# =============================================================================

# grabs the latlng of all the postal codes in Toronto
toronto_latlng = pd.read_csv('https://cocl.us/Geospatial_data')

# adds the lat lng values to the toronto_final dataFrame
toronto_final['Latitude'] = toronto_latlng['Latitude']
toronto_final['Longitude'] = toronto_latlng['Longitude']


print(toronto_final.shape)


import numpy as np
import pandas as pd 
from math import radians, cos, sin, asin, sqrt
import time

def haversine(pt, lat2=42.355589, lon2=-71.060175):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1 = pt[0]
    lat1 = pt[1]
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in miles
    return c * r

def get_distance(stations, trips):
    """
    Calculate the number of checkouts per station,
    and compute the distance of each station from a central location using the haversine formula.

    Calculates the number of checkouts for each station.
    Joins the checkout data with the station data.
    Computes the distance of each station from a central point (default is downtown Boston) using the haversine formula.
    Introduces pauses between each major step to avoid potential kernel crashes.

    Returns:
        pd.DataFrame: A DataFrame containing the station IDs, number of checkouts,
                      and distances to the central point.
    """
    # adding sleeps to prevent kernal crashes
    
    station_counts = np.unique(trips['strt_statn'].dropna(), return_counts=True)
    time.sleep(1)
    counts_df = pd.DataFrame({'id': station_counts[0], 'checkouts': station_counts[1]})
    time.sleep(1)
    counts_df = counts_df.join(stations.set_index('id'), on='id')
    time.sleep(1)
    # Add to the pandas dataframe the distance using the function we defined above and using map 
    counts_df.loc[:, 'dist_to_center'] = list(map(haversine, counts_df[['lng', 'lat']].values))
    return counts_df


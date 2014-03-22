from __future__ import absolute_import
from celery import shared_task

from .models import IPRecord, Distance

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 3960 mi is the radius of the Earth
    mi = 3960 * c
    return mi 

@shared_task
def calc_distance_task(my_ip_id, remote_ip_id):
    my_ip = IPRecord.objects.get(id=my_ip_id)
    remote_ip = IPRecord.objects.get(id=remote_ip_id)
    # Bonus: Create a Distance instance and record # miles
    miles = haversine(my_ip.lng, my_ip.lat, remote_ip.lng, remote_ip.lat)
    distance = Distance(miles=miles, from_ip=my_ip, to_ip=remote_ip)
    distance.save() 
    



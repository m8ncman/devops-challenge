from __future__ import absolute_import
from celery import shared_task

from .models import IPRecord


@shared_task
def calc_distance_task(my_ip_id, remote_ip_id):
    my_ip = IPRecord.objects.get(id=my_ip_id)
    remote_ip = IPRecord.objects.get(id=remote_ip_id)
    # Bonus: Create a Distance instance and record # miles

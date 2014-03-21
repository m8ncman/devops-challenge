import socket
from django.shortcuts import render

from .models import IPRecord
from .tasks import calc_distance_task


def index(request):

    my_ip = IPRecord.objects.get_or_create(address=socket.gethostbyname(socket.gethostname()))[0]
    remote_ip = IPRecord.objects.get_or_create(address=request.META['REMOTE_ADDR'])[0]

    calc_distance_task.delay(my_ip.id, remote_ip.id)

    return render(request, 'ipdistance/view.html', {
        'my_ip': my_ip,
        'remote_ip': remote_ip,
    })

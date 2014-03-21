from django.db import models


class IPRecord(models.Model):
    address = models.GenericIPAddressField(unique=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.lng and self.lat:
            return '%s (%s/%s)' % (self.address, self.lng, self.lat)
        return self.address


class Distance(models.Model):
    miles = models.FloatField(null=True)
    from_ip = models.ForeignKey(IPRecord, related_name='from_distances')
    to_ip = models.ForeignKey(IPRecord, related_name='to_distances')

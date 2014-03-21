from django.db import models


class IPRecord(models.Model):
    address = models.GenericIPAddressField(unique=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        if self.lng and self.lat:
            return '%s (%s/%s)' % (self.address, self.lng, self.lat)
        return self.address

from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return u'{}'.format(self.url)


class Location(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    class Meta:
        unique_together = ['city', 'country', 'region']

    def __unicode__(self):
        return u'{}, {}, {}'.format(self.city, self.country, self.region)


class View(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    page = models.ForeignKey(Page, related_name='views')
    location = models.ForeignKey(Location, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    count = models.IntegerField()

    def __unicode__(self):
        return u'{} from {} @ {}'.format(self.ip_address, self.location, self.date)
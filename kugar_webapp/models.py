from django.db import models
from django.db.models import TextField
# Create your models here.


class Feedkik(models.Model):
    title = TextField(blank=False)
    published_parsed = TextField(blank=False)
    links = TextField(blank=False)
    link = TextField(blank=False)
    torrent_seeds = TextField(blank=False)
    torrent_peers = TextField(blank=False)
    description = TextField(blank=False)
    magnet = TextField(blank=False)

    def __str__(self):
        return self.title
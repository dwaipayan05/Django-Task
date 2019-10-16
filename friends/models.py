from django.db import models

# Create your models here
class Names(models.Model):
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    friend_name = models.CharField(max_length=20)
    user_id = models.IntegerField()

    def _str_(self):
        return self.friend_name

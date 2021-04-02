from django.db import models
from django.utils import timezone

class Url(models.Model):
    title = models.CharField(max_length=200)
    urlName = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created = models.DateTimeField(editable=False)

    def x_ago(self):
        diff = timezone.now() - self.created
        return diff

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Url, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
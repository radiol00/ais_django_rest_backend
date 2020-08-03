from django.db import models
from django.conf import settings

# Create your models here.
class Absence(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=50)
    additional_info = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email, '{} - {}'.format(self.start_date, self.end_date);
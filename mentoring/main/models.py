from django.db import models

class users(models.Model):
    u_name = models.CharField(max_length=20)
    press_count = models.IntegerField(default=0)
from django.db import models


class User(models.Model):
    class Meta:
        db_table = "users"

    username = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField()

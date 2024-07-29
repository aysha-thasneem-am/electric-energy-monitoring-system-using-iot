from django.db import models

# Create your models here.


class Test(models.Model):
    uid = models.IntegerField()
    nm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'test'

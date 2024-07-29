from django.db import models

# Create your models here.



class Demo(models.Model):
    u_id = models.AutoField(primary_key=True)
    nm = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phn = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'demo'


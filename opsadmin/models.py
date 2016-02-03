from django.db import models

# Create your models here.
class Cloudhost(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    date = models.DateField()
    
    def __unicode__(self):
        return self.name

class Cloudhost_config(models.Model):
    name = models.ForeignKey(Cloudhost, on_delete=models.CASCADE)
    cpu = models.IntegerField()
    memory = models.IntegerField()
    disk = models.IntegerField()
    area = models.CharField(max_length=100)
    bandwidth = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    

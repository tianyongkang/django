from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=300)
    manager =  models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    
class Cloudhost(models.Model):
    host = models.CharField(max_length=100)
    intip = models.GenericIPAddressField()
    outip = models.GenericIPAddressField(blank=True, null=True)
    itemid = models.ForeignKey(Item)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    createdate = models.DateField()
    
    def __unicode__(self):
        return self.host

class Cloudhost_config(models.Model):
    hostid = models.ForeignKey(Cloudhost, on_delete=models.CASCADE)
    cpu = models.IntegerField()
    memory = models.IntegerField()
    disk = models.IntegerField()
    area = models.CharField(max_length=100)
    bandwidth = models.IntegerField()
    operateos = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.operateos

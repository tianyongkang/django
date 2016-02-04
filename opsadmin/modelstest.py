from opsadmin.models import Cloudhost
#import datetime


#t = Cloudhost(name = "ALY-online-30-10", ip = "11.1.30.10", date = datetime.datetime.now())
#t.save()
t = Cloudhost.objects.all()
print t
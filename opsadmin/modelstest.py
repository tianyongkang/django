from opsadmin.models import Cloudhost
#import datetime


#t = Cloudhost(name = "ALY-online-30-10", ip = "11.1.30.10", date = datetime.datetime.now())
#t.save()
print Cloudhost.objects.order_by('-date')[:5]
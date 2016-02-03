from django.contrib import admin

# Register your models here.
from opsadmin.models import Cloudhost, Cloudhost_config, Item

admin.site.register(Cloudhost)
admin.site.register(Cloudhost_config)
admin.site.register(Item)
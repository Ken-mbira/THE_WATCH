from django.contrib import admin

from neighbourhood.models import *

admin.site.register(Location)
admin.site.register(EventType)
admin.site.register(Services)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Occurrence)

# Register your models here.

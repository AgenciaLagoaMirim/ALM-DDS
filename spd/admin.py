from django.contrib import admin

from .models import DataParameter, Parameter, Station

admin.site.register(Station)
admin.site.register(DataParameter)
admin.site.register(Parameter)

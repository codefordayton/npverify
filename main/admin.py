from django.contrib import admin

# Register your models here.
from .models import NTEECategory, NTEECode, Nonprofit

admin.site.register(NTEECategory)
admin.site.register(NTEECode)
admin.site.register(Nonprofit)

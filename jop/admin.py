from django.contrib import admin

# Register your models here.
from .models import jop ,category , Apply
admin.site.register(jop)
admin.site.register(category)
admin.site.register(Apply)
from django.contrib import admin
from .models import Topic


# Register your models here.

# Upgrade Admin for adding new post
admin.site.register(Topic)

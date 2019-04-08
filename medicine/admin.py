from django.contrib import admin
from .models import User, Medication

admin.site.register([User, Medication])
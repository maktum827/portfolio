from django.contrib import admin
from .models import Post, Profile , Contact

# Register your models here.
admin.site.register((Post, Profile , Contact))
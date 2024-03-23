from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Product, Activity, DeleteRequest


admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Activity)
admin.site.register(DeleteRequest)
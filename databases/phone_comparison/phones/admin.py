from django.contrib import admin

# Register your models here.

from .models import Phone, ApplePhone, HuaweiPhone, AndroidPhone

admin.site.register(Phone)
admin.site.register(ApplePhone)
admin.site.register(HuaweiPhone)
admin.site.register(AndroidPhone)

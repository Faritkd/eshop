from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.SiteSetting)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.FooterLink)
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.ProjectReport)
admin.site.register(models.Category)
admin.site.register(models.Rate)
# admin.site.register(models.Donation)

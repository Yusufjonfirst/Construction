from django.contrib import admin

from pages.models import OurWorkModel


@admin.register(OurWorkModel)
class OurWorkModel(admin.ModelAdmin):
    list_display = ['cotegory']
    search_fields = ['cotegory']

from django.contrib import admin

from family_info.models import FamilyInfo


@admin.register(FamilyInfo)
class FamilyInfoAdmin(admin.ModelAdmin):
    list_display = ('tribe','origin')
    search_fields = ('tribe','origin')
from django.contrib import admin

from family_tree.models import FamilyTree


@admin.register(FamilyTree)
class FamilyTreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'creation_date')
    search_fields = ('name',)
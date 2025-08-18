from django.contrib import admin

from tree_share.models import TreeShare


@admin.register(TreeShare)
class TreeShareAdmin(admin.ModelAdmin):
    list_display = ('tree','shared_with','access_type','shared_on')
    list_filter = ('access_type',)
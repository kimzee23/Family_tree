from django.contrib import admin

from member.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','tree','relation','birth_date','marital_status')
    list_filter = ('marital_status','tree')
    search_fields = ('name','relation')

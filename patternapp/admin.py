from django.contrib import admin
from .models import FileName, RegexPattern

admin.site.register(FileName)

admin.site.site_header = "Pattern Generator Admin"
admin.site.site_title = "Pattern Admin"
admin.site.index_title = "Welcome to Regex Control Panel"

@admin.register(RegexPattern)
class RegexPatternAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'pattern')

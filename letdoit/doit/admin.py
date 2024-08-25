from django.contrib import admin
from .models import *


@admin.register(Goal)
class DoitAdmin(admin.ModelAdmin):
    list_display = ('content', 'start_time', 'completion_time', 'cash_amount', 'user_email', 'friend_email')
    search_fields = ('content', 'user_email', 'friend_email')
    list_filter = ('start_time', 'completion_time', 'user_email', 'friend_email')

        

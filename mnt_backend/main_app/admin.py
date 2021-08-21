from django.contrib import admin
from .models import User
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ticker', 'investmentAmount',  'tickerarray')

admin.site.register(User, UsersAdmin)


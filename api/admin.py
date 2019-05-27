from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NyteUser
from .forms import NyteUserChangeForm, NyteUserCreationForm
from . import models

class NyteUserAdmin(UserAdmin):
    add_form = NyteUserCreationForm
    form = NyteUserChangeForm
    model = NyteUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

# Register your models here.
admin.site.register(NyteUser, NyteUserAdmin)
admin.site.register(models.Account)
admin.site.register(models.AccountInformation)
admin.site.register(models.Event)
admin.site.register(models.Identity)
admin.site.register(models.MenuItem)
admin.site.register(models.Special)
admin.site.register(models.Transaction)
admin.site.register(models.UserSession)
admin.site.register(models.Venue)
admin.site.register(models.WorksAt)

@admin.register(models.ProtoMenuItem)
class ProtoMenuAdmin(admin.ModelAdmin):
    list_display = ("name", "type")

@admin.register(models.ProtoOrder)
class ProtoOrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_num", "status")
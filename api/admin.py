from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NyteUser
from .forms import NyteUserChangeForm, NyteUserCreationForm

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
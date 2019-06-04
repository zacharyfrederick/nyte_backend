from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NyteUser
from .forms import NyteUserChangeForm, NyteUserCreationForm
from . import models

class NyteUserAdmin(UserAdmin):
    add_form = NyteUserCreationForm
    form = NyteUserChangeForm
    model = NyteUser
    list_display =  ('email', 
        "first_name",
        "last_name",
        "middle_name",
        "date_joined",
        "phone",
        "facebook_id",
        "gender",
        'user_type',  
        'birthday', 
        'is_age_verified', 
        'is_email_verified')
    list_filter = ('user_type', 'is_staff', 'is_active',)
    fieldsets = (
        ("User Data", {'fields': 
        ('email', 
        'password', 
        "first_name",
        "last_name",
        "middle_name",
        "date_joined",
        "phone",
        "facebook_id",
        "gender",
        'user_type', 
        'membership', 
        'birthday', 
        'is_age_verified', 
        'is_email_verified')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'user_type', 'birthday', 'is_age_verified', 'is_email_verified','is_staff', 'is_active')}
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
#admin.site.register(models.Venue)
admin.site.register(models.WorksAt)
admin.site.register(models.Verification)

@admin.register(models.ProtoMenuItem)
class ProtoMenuAdmin(admin.ModelAdmin):
    list_display = ("name", "item_type")
    list_filter = ("item_type",)

@admin.register(models.ProtoOrder)
class ProtoOrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_num", "status", "message_sent")

@admin.register(models.Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "music_type", "price_level", "crowd_size", "tagline", "markup_fee")
    search_fields = ("name", "music_type", "tagline", "description")
    

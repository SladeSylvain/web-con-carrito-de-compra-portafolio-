from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('edad', 'ciudad')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('email', 'edad', 'ciudad')}),
    )
    list_display = ('username', 'email', 'edad', 'ciudad', 'is_staff')
    search_fields = ('username', 'email', 'ciudad')

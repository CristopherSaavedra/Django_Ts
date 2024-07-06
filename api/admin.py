# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Distrito, Reporte

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nombre', 'apellido', 'email', 'phone_number', 'address', 'is_client')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nombre', 'apellido', 'email', 'phone_number', 'address', 'is_client', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'nombre', 'apellido', 'email', 'is_client', 'is_staff')
    search_fields = ('username', 'nombre', 'apellido', 'email')
    ordering = ('username',)

class DistritoAdmin(admin.ModelAdmin):
    list_display = ('nombre_distrito',)
    search_fields = ('nombre_distrito',)
    ordering = ('nombre_distrito',)

class ReporteAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'distrito', 'created_at', 'lat', 'long', 'direccion')
    search_fields = ('cliente__username', 'distrito__nombre_distrito', 'descripcion', 'direccion')
    ordering = ('-created_at',)
    list_filter = ('distrito', 'created_at')

admin.site.register(User, UserAdmin)
admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Reporte, ReporteAdmin)

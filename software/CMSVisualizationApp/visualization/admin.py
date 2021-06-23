from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


class LogoInline(admin.TabularInline):
    model = Logos

class NavbarInline(admin.TabularInline):
    model = Navbar


class BodyInline(admin.TabularInline):
    model = Body


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', )}),
        (_('Category'), {'fields': ('category',)}),
    )
    inlines = [LogoInline, NavbarInline, BodyInline]


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    fields = ('bg_color', 'font_color', 'site_setting')
    list_display = ('bg_color', 'font_color' )


@admin.register(Body)
class BodyAdmin(admin.ModelAdmin):
    fields = ('bg_color', 'site_setting')
    list_display = ('bg_color', )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fields = ('html', 'css')
    list_display = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )


@admin.register(ExternalDatabaseConnectionCredentials)
class ExternalDatabaseConnectionCredentialsAdmin(admin.ModelAdmin):
    fields = ('host', 'dbname', 'user', 'password',)


@admin.register(Graphs)
class GraphAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'query', 'connection')}),
        (_('Code'), {'fields': ('code',)}),
        (_('Card Dimensions'), {'fields': ('card_width', 'card_height')}),
        (_('Position'), {'fields': ('top', 'left')}),
        (_('Table'), {'fields': ('table',)}),
        (_('Information'), {'fields': ('description',)}),
        (_('Category'), {'fields': ('category',)}),
        (_('Status'), {'fields': ('active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'query', 'connection', ),
        }),
    )

    list_display = ('title', 'connection', 'category', 'active')

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def response_add(self, request, obj, post_url_continue=None):
        if '_addanother' not in request.POST and '_popup' not in request.POST:
            request.POST = request.POST.copy()
            request.POST['_continue'] = 1
        return super().response_add(request, obj, post_url_continue)
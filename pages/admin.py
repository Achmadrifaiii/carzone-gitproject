from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.photo.url))

    # mengganti nama yabel yabg tadinya thumbnail menjadi Photo
    thumbnail.short_description = 'Photo'

    # buat nampilin tabel admin, nampilin di admin
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date' )
    # agar bisa di klick id sama nama pada tabel admin
    list_display_links = ('id', 'thumbnail', 'first_name')
    # nampilin fitur search pada tabel admin
    search_fields = ('first_name', 'last_name', 'designation')
    # sama dn yg lain, tapi jgn lupa koma pada baris list_filter, semisal lipa gk bakal tampil si form filter
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)

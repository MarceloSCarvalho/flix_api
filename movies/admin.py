from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id','title','release_date','genre')
    search_fields = ('title','genre__name',)

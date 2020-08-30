from django.contrib import admin

from .models import *

class TravelLocationImageAdmin(admin.StackedInline):
    model = TravelLocationImage

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    class Meta:
       model = Travel

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    class Meta:
       model = Day

@admin.register(TravelLocation)
class TravelLocationAdmin(admin.ModelAdmin):
    inlines = [TravelLocationImageAdmin]
    class Meta:
       model = TravelLocation

class TravelLocationImageAdmin(admin.ModelAdmin):
    pass







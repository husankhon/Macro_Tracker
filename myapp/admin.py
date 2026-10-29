from django.contrib import admin
from .models import Food, FoodLog

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'carbs', 'fat')
    search_fields = ('name',)

@admin.register(FoodLog)
class FoodLogAdmin(admin.ModelAdmin):
    list_display = ('food', 'servings', 'added_at')
    list_filter = ('added_at',)
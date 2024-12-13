from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Shift, Volunteer  # Import your models

# Register Shift model
@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'start_time', 'end_time', 'max_volunteers', 'volunteers_list')
    search_fields = ('event_name',)
    list_filter = ('date',)

    def volunteers_list(self, obj):
        return ", ".join([volunteer.user.username for volunteer in obj.volunteers.all()])
    volunteers_list.short_description = "Volunteers"

# Optional: Register Volunteer model as well
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'total_hours')

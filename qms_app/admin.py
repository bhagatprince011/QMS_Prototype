from django.contrib import admin
from .models import UserTypes, Users, Roles, Milestones, RoadTypes, Roads

# Customizing the admin panel to hide date_created and date_updated fields

class UserTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Exclude date_created and date_updated

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'user_type')  # Exclude date_created and date_updated

    # Ensuring password is hashed
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only hash the password if the user is new
            obj.set_password(obj.password)  # Hash the password before saving
        super().save_model(request, obj, form, change)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Exclude date_created and date_updated

class MilestonesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'next_milestone')  # Exclude date_created and date_updated

class RoadTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')  # Exclude date_created and date_updated

class RoadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'source', 'destination', 'road_type', 'contractor', 'engineer', 'milestone')  # Exclude date_created and date_updated

# Registering the models with the customized admin classes
admin.site.register(UserTypes, UserTypesAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Milestones, MilestonesAdmin)
admin.site.register(RoadTypes, RoadTypesAdmin)
admin.site.register(Roads, RoadsAdmin)

admin.site.site_header = "QMS Admin Portal"  # Change the header text
admin.site.site_title = "QMS Administration"  # Title in browser tab
admin.site.index_title = "Welcome to the QMS Admin Dashboard" 
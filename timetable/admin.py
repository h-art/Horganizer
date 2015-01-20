from django.contrib import admin
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from timetable.models import Period, Job, Role, Employee

class PeriodAdminForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = "__all__"

    def clean(self):
        # Validation goes here
        raise forms.ValidationError("TEST EXCEPTION!")

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

class PeriodAdmin(admin.ModelAdmin):
    form = PeriodAdminForm

# re-register admin model
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Role)
admin.site.register(Period, PeriodAdmin)
admin.site.register(Job)


from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin  # Import UnfoldModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm
from import_export.admin import ImportExportModelAdmin
from .models import StudentProfile, Team, Project, Report

@admin.register(Project)
class ProjectAdmin(UnfoldModelAdmin):  # Inherit from UnfoldModelAdmin
    list_display = ('title', 'projectid', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'projectid')
    list_filter = ('status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'projectid', 'description', 'objectives', 'motivation', 'area_of_work', 'supervisor_choices', 'team', 'status')
        }),
        ('Important dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    def get_project_information(self, obj):
        return obj.get_project_information()
    get_project_information.short_description = 'Project Information'
    get_project_information.allow_tags = True

@admin.register(Report)
class ReportAdmin(UnfoldModelAdmin):  # Inherit from UnfoldModelAdmin
    list_display = ('project', 'reportid', 'status', 'created_at', 'updated_at')
    search_fields = ('project', 'reportid')
    list_filter = ('status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('project', 'reportid', 'team', 'submitted_by', 'report', 'status')
        }),
        ('Important dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    def get_report_information(self, obj):
        return obj.get_report_information()
    get_report_information.short_description = 'Report Information'
    get_report_information.allow_tags = True

@admin.register(StudentProfile)
class StudentProfileAdmin(UnfoldModelAdmin,ImportExportModelAdmin):  
    ID='student_id'
    
    list_display = ( 'student_id','studentname','department','session', 'section',)
    search_fields = ('user', 'student_id')
    list_filter = ('department', 'level', 'session', 'section')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'student_id', 'phone', 'department', 'level', 'session', 'section', 'cgpa')
        }),
        ('Important dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    import_form_class = ImportForm
    export_form_class = ExportForm
    def get_student_information(self, obj):
        return obj.get_student_information()
    get_student_information.short_description = 'Student Information'
    get_student_information.allow_tags = True

@admin.register(Team)
class TeamAdmin(UnfoldModelAdmin):  # Inherit from UnfoldModelAdmin
    list_display = ('teamid', 'teamname', 'teamleader', 'created_at', 'updated_at')
    search_fields = ('teamid', 'teamname')
    list_filter = ('teamleader',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('teamid', 'teamname', 'teamleader', 'teammembers')
        }),
        ('Important dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    def get_team_information(self, obj):
        return obj.get_team_information()
    get_team_information.short_description = 'Team Information'
    get_team_information.allow_tags = True
    


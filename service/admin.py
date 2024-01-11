from django.contrib import admin
from service.models import Service, Parametr, Benefit, BeforeAfter, Question, Appointment, Feedback, RequestOfLeave, Setting, Team, Sale


class ParametrInline(admin.TabularInline):
    model = Parametr
    extra = 1

class BenefitInline(admin.TabularInline):
    model = Benefit
    extra = 1

class BeforeAfterInline(admin.TabularInline):
    model = BeforeAfter
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_filter = ['category']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}
    inlines = [ParametrInline, BenefitInline, QuestionInline, BeforeAfterInline]
    save_on_top = True
    save_as = True
    
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     search_fields = ['name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_filter = ['date']
    search_fields = ['name']
admin.site.register(RequestOfLeave)  
admin.site.register(Setting)  
admin.site.register(Sale)  

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ['name']
    


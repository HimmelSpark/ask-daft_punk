from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from questions.models import *

# Register your models here.

def count(obj):
    return Question.objects.filter(author=obj).count()

class ProfileAdmin(admin.ModelAdmin):

    # class QuestionFilter(SimpleListFilter):
    #     title = 'Has Questions'
    #     parameter_name = 'count'
    #
    #     def lookups(self, request, model_admin):
    #         return [('YES', 'YES'), ('NO', 'NO')]
    #     def queryset(self, request, queryset):
    #         # if self.value() == "YES":
    #         #     return queryset.filter(profile__count > 0)
    #         if self.value() == "NO":
    #             return queryset.filter(profile__count=0)

    raw_id_fields = ("usr_key",)
    list_display = ('avatar', 'usr_key', count)
    list_filter = ('usr_key__email',)
    search_fields = [('usr_key')]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('author', 'header')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Like)
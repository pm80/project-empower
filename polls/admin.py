from django.contrib import admin

from .models import Question, Choice, LoginInfo, Blog, Entry, Author, EntryDetail, Person, Group, Membership, Author2, Store, OpinionPoll, Response,  Publisher, Book, Publication

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

'''class LoginInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('login information', {'fields':['user','password']})
        ]'''
class BookAdmin(admin.ModelAdmin):
	list_display = ['name','id']
class PublisherAdmin(admin.ModelAdmin):
	list_display = ['name','id']
admin.site.register(OpinionPoll)
admin.site.register(Response)
admin.site.register(LoginInfo)
admin.site.register(Choice)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(EntryDetail)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Author2)
admin.site.register(Publication)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Store)

admin.site.register(Question, QuestionAdmin)

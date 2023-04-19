from django.contrib import admin
from .models import *
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

# Register your models here.
class futureData(admin.ModelAdmin):
    list_display= ('chart_type','data','date')
class News_display(admin.ModelAdmin):
    list_display= ('chart','relevance_level','title','link','website','date','image','archive')
    fields = ['chart','relevance_level','title','link','website','archive']
class Updated_news(admin.ModelAdmin):
    list_display= ('tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','title','link','website','date','image','archive')
    fields = ['tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','title','link','website','archive']
class tweet_display_ticker(admin.ModelAdmin):
    list_display= ('tweet_link','tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','archive')
    fields = ['tweet_link','tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','archive']
class tweet_display_index(admin.ModelAdmin):
    list_display= ('tweet_link','chart','relevance_level','archive')
    fields = ['tweet_link','chart','relevance_level','archive']
class email_display(admin.ModelAdmin):
    list_display= ('email','archive')
    fields = ['email','archive']
class News_recc(admin.ModelAdmin):
    list_display= ('tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','link','website','date','archive')
    fields = ['tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','link','website','date','archive']
# class News_recc(admin.ModelAdmin):
#     list_display= ('tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','title','link','website','archive')
#    fields = ['tab_name','relevance_level_tab','on_landing_page','relevance_level_landing_page','title','link','website','archive']


# admin.site.unregister(Group) 
admin.site.site_header = 'Texisle Admin Panel'
admin.site.site_title  =  "Texisle Admin Panel site"
admin.site.index_title  =  "Texisle Admin Panel"

admin.site.register(News_rec,News_recc)
admin.site.register(emails,email_display)


# admin.site.register(News,News_display)
# admin.site.register(News_data, Updated_news)
# admin.site.register(tweet_table_ticker_test, tweet_display_ticker)
# admin.site.register(tweet_table_index_test, tweet_display_index)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

from django.contrib import admin
from django.urls import path, include
from home import views 



#django admin header customization
admin.site.site_header = "Developer Harsh"
admin.site.site_title = "Welcome to Dashboard"
admin.site.site_index = "Welcome to this Portal"
urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('project', views.project, name='project'),
]
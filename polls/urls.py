from django.conf.urls import url
from polls import views
app_name = 'polls'
urlpatterns = [
url(r'^$', views.login_page, name='login_page'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^signup_fun/$', views.signup_fun, name='signup_fun'),
url(r'^check/$', views.check, name='check'), 
url(r'^moreInfo/$', views.moreInfo, name='moreInfo'), 
url(r'^moreInfoUpdate/$', views.moreInfoUpdate, name='moreInfoUpdate'), 
url(r'^database/$', views.database, name='database'), 


]

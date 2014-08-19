from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from school import viewsets
from Accounts import views

#from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

router = DefaultRouter()
router.register(r'teachers', viewsets.TeacherViewSet)
router.register(r'students', viewsets.StudentViewSet)
router.register(r'users', views.CustomUserViewSet)

urlpatterns = patterns('school.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^teachers/$', views.TeacherList.as_view()),
    #url(r'^teachers/(?P<pk>[0-9]+)$', views.TeacherDetail.as_view()),
    #url(r'^users/$', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #url(r'^students/$', views.StudentList.as_view()),
    #url(r'^students/(?P<pk>[0-9]+)$', views.StudentDetail.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
)

#urlpatterns = format_suffix_patterns(urlpatterns)

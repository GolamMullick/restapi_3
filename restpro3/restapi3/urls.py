from django.urls import path
from django.urls import include
from . import views
from rest_framework_nested import routers


router=routers.DefaultRouter()
router.register('students',views.StudentView,base_name='students')
router.register('schools',views.SchoolView,base_name='schools')


school_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
school_router.register(r'students', views.StudentView,base_name='students')


urlpatterns = [
   path('', include(router.urls)),
   path('', include(school_router.urls))

]

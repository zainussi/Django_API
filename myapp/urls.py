from django.urls import include,path
from rest_framework import routers
from . import views
#from .views import upload_file_view

app_name = 'myapp'

routers = routers.DefaultRouter()
routers.register(r'QA', views.QAViewSet)
urlpatterns = [
    path('', include(routers.urls)),
    path('api_auth/', include(('rest_framework.urls'), namespace='rest_framework')),
    #path('uploadfile/', upload_file_view, name='upload-view'),
]
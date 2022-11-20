from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from trivia import views

router = routers.DefaultRouter()
#router.register(r'questions', views.QuestionViewSet)
router.register(r'examen', views.ExamenViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('examen/', admin.site.urls) #URL de examen
]
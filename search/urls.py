from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^error', views.error, name='error'),
    url(r'^result/fitness-motivation', views.result_fitnessmotivation, name='fitnessmotivation'),
    url(r'^result/b/fitness-motivation', views.result_fitnessmotivation_blur, name='fitnessmotivation-blur'),
    url(r'^result/pets', views.result_pets, name='pets'),
    url(r'^result/b/pets', views.result_pets_blur, name='pets-blur'),
]
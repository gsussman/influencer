from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^error', views.error, name='error'),
    url(r'^result/fitness-motivation', views.result_fitnessmotivation, name='fitnessmotivation'),
    url(r'^result/b/fitness-motivation', views.result_fitnessmotivation_blur, name='fitnessmotivation-blur'),
    url(r'^result/pets', views.result_pets, name='pets'),
    url(r'^result/b/pets', views.result_pets_blur, name='pets-blur'),
    url(r'^result/autotest', views.result_autotest, name='autotest'),
    url(r'^result/digital-marketing', views.result_digital_marketing, name='digital-marketing'),
#    url(r'^result/<nichelist>', views.result, name='result'),
    url(r'^result/mental-health', views.result_mental_health, name='mental-health'),
    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
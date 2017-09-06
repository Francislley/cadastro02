from django.conf.urls import url
from .views import get_funcionarios

urlpatterns = [

    url(r'^$', get_funcionarios),
]

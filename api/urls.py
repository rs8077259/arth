from django.urls import path
from . import views
urlpatterns=[
    path("meaning/<str:WordLanguage>/<str:MeaningLanguage>/<str:word>",views.API.as_view(
        {
            'get' : 'retrieve',
            'post' : 'create',
            'put' : 'update',
            'patch' : 'partial_update',
        }
    ))
]
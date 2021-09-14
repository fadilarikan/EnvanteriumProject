from django.urls import path, include

from envapp.api.views import ProductListAPIView

urlpatterns = [
    path('list', ProductListAPIView.as_view(),name='list'),

]
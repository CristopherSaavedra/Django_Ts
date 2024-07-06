
from django.urls import path
from .views import *


urlpatterns = [

    path('list/reporte/', ReporteListView.as_view(), name='reporte-list'),
    # path('reportes/', ReporteCreateView.as_view(), name='reporte-create'),
    path('list/user/', UserListView.as_view(), name='user-list'),
    path('list/distrito/', DistritoListView.as_view(), name='distrito-list'),

    path('register/client/', RegisterClientAPIView.as_view(), name='register_client_api'),
    path('login/client/', LoginClientAPIView.as_view(), name='login_client_api'),

    path('register/distrito/', RegisterDistritoAPIView.as_view(), name='register_distrito_api'),
    path('register/reporte/', RegisterReporteAPIView.as_view(), name='register_distrito_api'),


]
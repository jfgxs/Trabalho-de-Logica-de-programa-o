from django.urls import path
from .views import upload_pdf, baixar_txt

urlpatterns = [
    path('', upload_pdf, name='upload_pdf'),
    path('baixar/<str:nome_txt>/', baixar_txt, name='baixar_txt'),
]
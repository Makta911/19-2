from django.urls import path
import django.urls
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contact')
]

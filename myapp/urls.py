from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="enterprise"),     
    path("institutions/", views.institutions, name="institutions"),     
    path("bond/", views.bond, name="bond"),     
    path("industry/", views.industry, name="industry"),     
    path("macro/", views.macro, name="macro"),     
    path("benchmark/", views.benchmark, name="benchmark"),     
    path("other/", views.other, name="other"),
    path("download/", views.download_file, name="download")
]


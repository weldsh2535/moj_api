from reports import views
from django.urls import path

urlpatterns = [
    path('ReportInfo', views.create_report, name='create_report'),
    path('TotalReport', views.get_total_report, name='create_report'),
    path('reports/<str:username>/reports/',views.get_report_by_username,name='report_by_username'),
    path('ReportInfos',views.get_report, name='get_report'),

]
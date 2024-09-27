from django.urls import path
from solutions import views

urlpatterns = [
    path('solution', views.create_solution, name='create_solution'),
    path('solutions', views.get_solution,name='get_solution'),
    path('solution/<int:pk>',views.get_solution_by_id,name='get_solution'),
    path('solution/<int:pk>',views.update_solution,name='update_solution'),
    path('solution/<int:pk>',views.delete_solution,name='delete_solution'),
    path('solution/<int:report_id>',views.get_solutions_by_report_id,name='get_solution_by_report'),
    path('solution/<int:report_id>', views.update_solutions_by_report_id,name='update_solutions_by_report'),
    path('solution/<int:report_id>', views.delete_solutions_by_report_id,name='delete_solutions_by_report'),
    path('solution/<int:user_id>/reports/',views.get_solutions_by_user_id_reports,name='get_solutions_by_user_id_reports'),
    path('solution/<int:report_id>/solution/',views.get_solution_by_report_id,name='get_solution_by_report'),
]
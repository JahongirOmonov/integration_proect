from django.urls import path
from .views import EmployeeListView



urlpatterns = [
    path('workers/', EmployeeListView.as_view(), name='get_employees'),
]

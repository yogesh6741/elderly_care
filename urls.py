from django.urls import path
from . import views

urlpatterns = [
    path('elderly/<int:elderly_person_id>/medications/', views.medication_list, name='medication_list'),
    path('medications/<int:medication_id>/send_reminder/', views.send_medication_reminder, name='send_medication_reminder'),
]

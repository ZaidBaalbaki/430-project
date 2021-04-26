from django.urls import path
from . import views
from user.views import logout

urlpatterns = [
    path('editClinic/<uuid:id>/', views.Clinic_edit),
    path('changePassword/<uuid:id>/', views.changePassword),
    path('Clinic/<uuid:id>/', views.Clinic_profile),
    path('waitingApp/<uuid:hos_id>/', views.waiting_app),
    path('count/<uuid:hos_id>/', views.count),
    path('listClinic/',views.listClinic),
    path('confirm_appointments_now/<uuid:appointment_id>/', views.confirm_appointments_now),
    path('complete_appointments_now/<uuid:appointment_id>/', views.complete_appointments_now),
    path('reject_appointments_now/<uuid:appointment_id>/', views.reject_appointments_now),
    path('addHoliday/<uuid:id>/',views.addHoliday),
]

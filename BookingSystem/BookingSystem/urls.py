

from django.contrib import admin
from django.urls import path
from bus_booking_managment import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', views.book.as_view(), name='booking-list-create'),
    path('seats/<int:trip_id>/', views.get_seats.as_view(), name='available-seat-list'),
]

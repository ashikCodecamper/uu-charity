from django.urls import path

from . import views

urlpatterns = [
    path('', views.charity, name="index"),
    path('details/<int:id>', views.details, name='details'),
    path('events/', views.events, name='events'),
    path('events/<int:charity_id>/', views.events, name='events_by_charity'),
    path('donate/<int:id>', views.donate, name='donate'),
    path('handle_donate/', views.handle_donate, name='handle_donate'),

]
from django.urls import path
from service import views
urlpatterns = [
    path('', views.index, name='index'),
    path('after_before/', views.after_before, name='after_before'),
    path('confidentialitly/', views.confidentialitly, name='confidentialitly'),
    path('sale/', views.sale, name='sale'),
    path('price_list/', views.price_list, name='price_list'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('add_request_of_leave/', views.add_request_of_leave, name='add_request_of_leave'),
]
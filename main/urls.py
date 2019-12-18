from django.urls import path

from main.views import *


urlpatterns = [
    path('phones/', PhoneViewList.as_view()),
    path('phone_details/<int:id>/', PhoneViewDetails.as_view()),
    path('phone/', PhoneViewAddDelete.as_view()),
    path('phone/<int:id>/', PhoneViewAddDelete.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('cart/', CartView.as_view()),
    path('cart/<int:id>/', CartView.as_view()),
    path('cart_del/<int:id>/', CartRemView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:id>/', OrderView.as_view()),
    path('', index, name='index'),
]

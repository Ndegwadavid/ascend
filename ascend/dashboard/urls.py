from django.urls import path
from .views import dashboard_view
from . import views


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    #path('forex_trading/', views.forex_trading, name='forex_trading'),
    #path('local_currency/', views.local_currency, name='local_currency'),
    #path('crypto_investment/', views.crypto_investment, name='crypto_investment'),
    #path('portfolio/', views.portfolio, name='portfolio'),
    #path('market_analysis/', views.market_analysis, name='market_analysis'),
    #path('notifications/', views.notifications, name='notifications'),
    #path('settings/', views.settings, name='settings'),
    #path('logout/', views.logout_view, name='logout_view'),
]
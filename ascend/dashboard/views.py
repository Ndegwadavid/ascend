from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

#def forex_trading(request):
#    return render(request, 'forex_trading.html')
#
#def local_currency(request):
#    return render(request, 'local_currency.html')
#
#def crypto_investment(request):
#    return render(request, 'crypto_investment.html')
#
#def portfolio(request):
#    return render(request, 'portfolio.html')
#
#def market_analysis(request):
#    return render(request, 'market_analysis.html')
#
#def notifications(request):
#    return render(request, 'notifications.html')
#
#def settings(request):
#    return render(request, 'settings.html')
#
#def logout_view(request):
#    # Handle logout logic here
#    return redirect('home')  # Redirect to home or login page
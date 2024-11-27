from django.urls import path
from .views import IndexView, AboutView, ServiceView, PortfolioView, BlogView, ContactView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('', AboutView.as_view(), name='about'),
    path('service/', ServiceView.as_view(), name='service'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('contact/', ContactView.as_view(), name='contact')

]

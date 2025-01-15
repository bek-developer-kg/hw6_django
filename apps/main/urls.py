from django.urls import path
from apps.main.views import index, about, contact, faq, about_me

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('about_me/', about_me, name='about_me')
]

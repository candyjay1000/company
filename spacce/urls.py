from django.urls import path
from .views import * 

urlpatterns = [
    path('', index,name='homepage'),
    path('about', about,name='about_us'),
    path('contact',contact ,name='contact_us'),
    path('services', services,name='service'),
    path('team',team ,name='teams'),
    path('pricing',pricing ,name='price'),
    path('portfolio',portfolio ,name='portfolios'),
    path('portfolio-detail',portfolio_details,name='portfolio-details'),
    path('testimonials',testimonials ,name='testimonials'),
    path('blog',blog,name='blogs'),
    path('blog-single',blog_single ,name='blog-single')
]

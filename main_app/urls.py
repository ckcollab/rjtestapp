


from django.urls import path
from . import views
from .views import (home_view,readings_view,bookdetail_view)
from django.conf.urls.static import static
from django.conf import settings



app_name = 'main_app'

urlpatterns = [
    path('', home_view.as_view(),name='home'),
   # path('projects/', projects_view.as_view(),name='projects'),
   # path('travel/', travel_view.as_view(),name="travel"),
   # path('thank_you/', thankyou_view.as_view(),name="thank_you"),
   # path('contact/', ContactFormView.as_view(), name="contact"),
   # path('article/<int:pk>', traveldetail_view.as_view(), name="article-detail"),
   # path('aboutme/', aboutme_view.as_view(),name='aboutme'),
    path('readings/', readings_view.as_view(),name='readings'),
    path('book/<int:pk>', bookdetail_view.as_view(),name='book-detail'),
]



from django import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

from .views import (
    LoginUser, RoomListView, order_create, register, logout_user, total_cost, user_profile
)
urlpatterns = [
    path('', RoomListView.as_view(), name='mainpage' ),
    path('selectdate/', order_create , name='selectdate'),
    path('register/', register, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('totalcost/',  total_cost, name='totalcost'),
    path('profile/<username>', user_profile, name='user_profile'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
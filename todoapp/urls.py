from django.urls import path
from .views import index, created, login_view, logout_view, registration, edit, delete
# from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path("", index, name="index"),
    path("created/", created, name="created"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', registration, name='registration'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    # path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
]

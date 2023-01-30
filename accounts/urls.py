from django.urls import path, include

from accounts import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    
    path('', include('django.contrib.auth.urls')),

    path("<int:pk>/", views.UserDetailView.as_view(), name="profile"),
    path("<int:pk>/edit/", views.UserUpdateView.as_view(), name="edit-profile"),
]
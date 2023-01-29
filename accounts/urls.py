from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),

    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="profile"),
    path("<int:pk>/edit/", views.UserUpdateView.as_view(), name="edit-profile"),
]
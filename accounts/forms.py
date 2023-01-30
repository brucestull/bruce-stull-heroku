from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            # Don't need to provide first_name and last_name at registration.
            # Can add these fields later, if preferred.
            # 'first_name',
            # 'last_name',
        )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',

            # 'is_staff',   # This field should only be available to
            # some adminstrative role. There would be some sort of page
            # where the andminstrative role can change the role of a user.

            # 'is_superuser',   # This field should only be available to
            # some adminstrative role. There would be some sort of page
            # where the andminstrative role can change the role of a user.
        )
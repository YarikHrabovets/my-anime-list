from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import AuthenticationForm
from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput
from django_countries.widgets import CountrySelectWidget

from .models import AnilistUser, Profile


class AnilistUserCreationForm(UserCreationForm):
    captcha = CaptchaField(
        label='Security captcha',
        widget=CaptchaTextInput(attrs={'class': 'form-control', 'placeholder': 'Captcha...'})
    )

    def __init__(self, *args, **kwargs):
        super(AnilistUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password...'}
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password Confirmation...'}
        )

    class Meta:
        model = AnilistUser
        fields = ('email', 'username')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email...'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username...'}),
        }


class AnilistUserAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField(
        label='Security captcha',
        widget=CaptchaTextInput(attrs={'class': 'form-control', 'placeholder': 'Captcha...'})
    )

    def __init__(self, *args, **kwargs):
        super(AnilistUserAuthenticationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email...'}
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password...'}
        )


class AnilistUserChangeForm(UserChangeForm):
    pass


class ProfileChangeForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('NONE', 'none'),
        ('MALE', 'male'),
        ('FEMALE', 'female')
    ]
    gender = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-control'}), choices=GENDER_CHOICES)

    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'gender', 'country')
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'country': CountrySelectWidget()
        }


from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации"""
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleFormMixin, ModelForm):
    """Форма для модели User"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'phone', 'country')
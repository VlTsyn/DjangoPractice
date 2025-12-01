
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import UserRegisterForm


class RegisterView(CreateView):
    template_name = 'users/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:catalog')
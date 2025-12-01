from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class RegisterView(CreateView):
    template_name = 'users/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:catalog')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'Testmail123987@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_profile.html'
    context_object_name = 'user'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('users:user_profile', kwargs={'pk': self.object.pk})
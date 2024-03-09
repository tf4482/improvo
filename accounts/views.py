from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):

        username = form.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            form.add_error('username', 'This username is already taken.')
            return self.form_invalid(form)
        else:
            return super().form_valid(form)

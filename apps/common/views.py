from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .forms import SignUpForm
from django.urls import reverse_lazy

#La seguente classe consente la navigazione delle pagine solo quando loggate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url =  reverse_lazy('home')
    template_name = 'common/register.html'

#Per usare LoginRequireMixin utilizzarlo come primo elemento da cui derivare la classe della view che
#dovrà essere navigabile solo sotto autenticazione
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('login')

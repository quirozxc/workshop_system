from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
#
from user.forms import CustomPasswordChangeForm

# Create your views here.
class CustomPasswordChangeView(PasswordChangeView):
  form_class = CustomPasswordChangeForm
  template_name = 'user/change_password.html'
  success_url = reverse_lazy('home_page')
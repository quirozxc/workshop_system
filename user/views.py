from django.views import generic
#
from user.models import User

# Create your views here.
class UserListView(generic.ListView):
    model = User
#
class UserDetailView(generic.DetailView):
    model = User
#
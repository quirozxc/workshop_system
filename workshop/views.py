from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
#
from order.models import RepairOrder

# Create your views here.
class HomePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #
        if request.user.is_superuser: return HttpResponseRedirect('admin')
        #
        return render(
            request=request,
            template_name='workshop/home_page.html',
            context={'latest_order': RepairOrder.objects.filter()}
        )
    #
#
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.conf import settings
#
from .models import Assignment
# Create your views here.
class HomePageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #
        if request.user.is_superuser:
            return HttpResponseRedirect('admin')
        #
        elif request.user.groups.filter(name=settings.MANAGER_NAME):
            return HttpResponseRedirect('management')
        #
        elif request.user.groups.filter(name=settings.DELEGATE_NAME):
            # pending_assignment_list = request.user.pending_assignments()
            # pending_guarantee_list = request.user.pending_assignments(just_guarantee=True)
            pending_assignment_list = request.user.pending_all_assignments()
        #
        else: raise PermissionDenied
        #
        return render(
            request=request,
            template_name='workshop/home_page.html',
            context={
                'pending_assignment_list': pending_assignment_list,
            }
        )
    #
#
class ManagementView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        #
        return render(
            request=request,
            template_name='workshop/management.html',
            context={'latest_order': Assignment.get_pendings()}
        )
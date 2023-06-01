from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView
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
            return PendingView.as_view()(request)
        #
        raise PermissionDenied
    #
#
class PendingView(ListView):
    model = Assignment
    template_name = 'workshop/home_page.html'
    context_object_name = 'pending_assignment_list'
    paginate_by = 3
    #
    def get_queryset(self):
        if self.request.user.groups.filter(name=settings.DELEGATE_NAME):
            return self.request.user.pending_all_assignments()
        raise PermissionDenied
    #
#
class ReviewedView(ListView):
    model = Assignment
    template_name = 'workshop/reviewed.html'
    context_object_name = 'reviewed_assignment_list'
    paginate_by = 3
    #
    def get_queryset(self):
        if self.request.user.groups.filter(name=settings.DELEGATE_NAME):
            return self.request.user.reviewed_assignments()
        raise PermissionDenied
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
    #
#
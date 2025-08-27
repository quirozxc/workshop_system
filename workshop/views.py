from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.conf import settings
from django.db.models import Q
#
from django.utils import timezone
#
from .models import Assignment, Invoice, Note
from .forms import CreateInvoiceForm, UpdateInvoiceForm
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_assignment'] = self.get_queryset().count()

        return context
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
        elif self.request.user.groups.filter(name=settings.MANAGER_NAME):
            return self.model.get_all_reviewed()
        raise PermissionDenied
    #
#
class InvoicedView(ListView):
    model = Assignment
    template_name = 'workshop/invoiced.html'
    context_object_name = 'invoiced_assignment_list'
    paginate_by = 3
    #
    def get_queryset(self):
        if self.request.user.groups.filter(name=settings.DELEGATE_NAME):
            return self.request.user.invoiced_assignments()
        elif self.request.user.groups.filter(name=settings.MANAGER_NAME):
            return self.model.get_all_invoiced()
        raise PermissionDenied
    #
#
class ManagementView(LoginRequiredMixin, ListView):
    model = Assignment
    template_name = 'workshop/management.html'
    context_object_name = 'pending_assignment_list'
    paginate_by = 3
    #
    def get_queryset(self):
        if self.request.user.groups.filter(name=settings.MANAGER_NAME):
            return self.model.get_all_pending()
        raise PermissionDenied
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_assignment'] = self.get_queryset().count()

        return context
    #
#
class SearchView(ListView):
    model = Assignment
    template_name = 'search_results.html'
    context_object_name = 'assignment_list'
    paginate_by = 3
    #
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q.isdigit(): q = int(q)
        querys = (
            Q(id__icontains=q) |
            Q(order__device__owner__dni__icontains=q) |
            Q(order__device__owner__phonenumber__number__icontains=q) |
            Q(order__device__owner__first_name__icontains=q) |
            Q(order__device__owner__last_name__icontains=q)
        )
        try: qs = Assignment.objects.filter(querys).order_by('id')
        except Assignment.DoesNotExist: qs = None
        finally: return qs
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
#
class CreateInvoiceView(CreateView):
    form_class = CreateInvoiceForm
    template_name = 'workshop/create_invoice.html'
    success_url = reverse_lazy('home_page')
    #
    def get_success_url(self):
        return self.success_url
    #
    def get_initial(self):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        return {
            'assignment': assignment,
        }
    #
    def form_valid(self, form):
        invoice = form.save(commit=False)
        if form.cleaned_data['is_picked']:
            invoice.pickup_date = timezone.now().date()
        invoice.save()
        if form.cleaned_data['note']:
            Note.objects.create(
                invoice=invoice,
                note=form.cleaned_data['note'],
            )
        #
        return redirect(self.get_success_url())
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = Assignment.objects.get(pk=self.kwargs['pk'])
        return context
    #
#
class UpdateInvoiceView(UpdateView):
    model = Assignment
    form_class = UpdateInvoiceForm
    template_name = 'workshop/update_invoice.html'
    success_url = reverse_lazy('home_page')
    #
    def get_success_url(self):
        return self.success_url
    #
    def get_initial(self):
        assignment = get_object_or_404(Assignment, pk=self.kwargs.get('pk'))
        return {
            'assignment': assignment,
            'amount': assignment.invoice.amount,
            'warranty_days': assignment.invoice.warranty_days,
            'is_picked': True if assignment.invoice.pickup_date else False,
            'note': assignment.invoice.get_note_or_none(),
        }
    #
    def form_valid(self, form):
        assignment = form.save()
        invoice = assignment.invoice
        invoice.amount = form.cleaned_data['amount']
        invoice.warranty_days = form.cleaned_data['warranty_days']
        if form.cleaned_data['is_picked']:
            if not invoice.was_picked:
                invoice.pickup_date = timezone.now().date()
        else: invoice.pickup_date = None
        invoice.save()
        if form.cleaned_data['note']:
            note, created = Note.objects.get_or_create(
                invoice=invoice,
            )
            note.note = form.cleaned_data['note']
            note.save()
        else: 
            try:
                Note.objects.get(invoice=invoice).delete()
            except Note.DoesNotExist:
                pass
            #
        #
        return redirect(self.get_success_url())
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignment'] = Assignment.objects.get(pk=self.kwargs['pk'])
        return context
    #
#
def delete_invoice(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    assignment.invoice.delete()
    return redirect(reverse_lazy('home_page'))
#
def create_guarantee(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    #
    assignment.order.was_reviewed=False
    assignment.order.save()
    #
    Assignment.objects.create(
        order=assignment.order,
        delegate=assignment.delegate,
        is_guarantee=True,
    )
    return redirect(reverse_lazy('home_page'))
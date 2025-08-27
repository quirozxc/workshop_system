from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from .models import RepairOrder
from user.models import User
from workshop.models import Assignment

from .forms import CreateRepairOrderMultiForm, UpdateRepairOrderMultiForm

# Create your views here.
class CreateRepairOrderView(CreateView):
    form_class = CreateRepairOrderMultiForm
    template_name = 'order/create.html'
    success_url = reverse_lazy('home_page')

    def get_success_url(self):
        return self.success_url
    
    def form_valid(self, form):
        user, created = User.objects.get_or_create(
            dni=form['user'].cleaned_data['dni'],
        )
        if created:
            user.first_name = form['user'].cleaned_data['first_name']
            user.last_name = form['user'].cleaned_data['last_name']
            user.save()
            #
            phone_number=form['phone_number'].save(commit=False)
            phone_number.user = user
            phone_number.save()
            #
        else:
            phone_number = form['phone_number'].save(commit=False)
            #
            user.phonenumber.idc = phone_number.idc
            user.phonenumber.number = phone_number.number
            user.phonenumber.is_whatsapp_number = phone_number.is_whatsapp_number
            #
            user.phonenumber.save()
        #
        device = form['device'].save(commit=False)
        repair_order = form['repair_order'].save(commit=False)
        assignment = form['assignment'].save(commit=False)
        #
        device.owner = user
        device.save()
        #
        repair_order.device = device
        repair_order.save()
        # repair_order.failture.set(form['repair_order'].cleaned_data['failture'])
        #
        assignment.order = repair_order
        assignment.save()
        #
        return redirect(self.get_success_url())
    #
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form['assignment'].fields['is_guarantee'].disabled = True
        return form
    #
#
class UpdateRepairOrderView(UpdateView):
    model = Assignment
    form_class = UpdateRepairOrderMultiForm
    template_name = 'order/update.html'
    success_url = reverse_lazy('home_page')
    #
    def get_form_kwargs(self):
        kwargs = super(UpdateRepairOrderView, self).get_form_kwargs()
        kwargs.update(
            instance={
                'user': self.object.order.device.owner,
                'phone_number': self.object.order.device.owner.phonenumber,
                'device': self.object.order.device,
                'repair_order': self.object.order,
                'assignment': self.object,
                'note': self.object.order.has_note_or_none(),
            }
        )
        return kwargs
    #
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form['assignment'].fields['is_guarantee'].disabled = True
        return form
    #

    def form_valid(self, form):
        redirect_url = super().form_valid(form)
        note = self.object['note']
        if note.note:
            repair_order = self.object['repair_order']
            if not repair_order.has_note_or_none():
                note.repair_order = repair_order
                note.save()
            #
        else: note.delete()
        return redirect_url
#
def mark_as_reviewed(request, pk):
    order = get_object_or_404(RepairOrder, pk=pk)
    order.was_reviewed = True
    order.save()
    return redirect(reverse_lazy('home_page'))
#
def mark_as_returned(request, pk):
    order = get_object_or_404(RepairOrder, pk=pk)
    order.is_active = False
    order.save()
    return redirect(reverse_lazy('home_page'))
#
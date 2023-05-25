from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

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
        #
        phone_number = form['phone_number'].save(commit=False)
        device = form['device'].save(commit=False)
        repair_order = form['repair_order'].save(commit=False)
        assignment = form['assignment'].save(commit=False)
        #
        device.owner = phone_number.user = user
        #
        phone_number.save()
        device.save()
        #
        repair_order.device = device
        repair_order.save()
        repair_order.failture.set(form['repair_order'].cleaned_data['failture'])
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
                'phone_number': self.object.order.device.owner.phonenumber_set.last(),
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
#
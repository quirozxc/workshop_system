from django.shortcuts import render
from django.views.generic.base import View

from .forms import RepairOrderForm

# Create your views here.
class RepairOrderView(View):
    def get(self, request, *args, **kwargs):
        form = RepairOrderForm()
        return render(
            request=request,
            template_name='order/create.html',
            context={
                'form': form,
            }
        )
    #
#
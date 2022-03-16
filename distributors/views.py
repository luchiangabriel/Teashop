
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from distributors.models import Distributor


class CreateDistributorView(LoginRequiredMixin, CreateView):
    model = Distributor
    fields = ['name', 'email', 'telephone']
    template_name = 'distributors_form.html'

    def get_success_url(self):
        return reverse('distributors:adauga')


class DistributorsView(LoginRequiredMixin, ListView):
    model = Distributor
    template_name = 'distributors_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Distributor.objects.filter(active=True)


class UpdateDistributorView(UpdateView):
    model = Distributor
    fields = ['name', 'email', 'telephone']
    template_name = 'distributors_form.html'

    def get_queryset(self):
        return Distributor.objects.filter(active=True)

    def get_success_url(self):
        return reverse('distributors:lista_distribuitori')


@login_required
def deactivate_distributor(request, pk):
    if Distributor.objects.filter(id=pk).exists:
        Distributor.objects.filter(id=pk).update(active=False)
    return redirect('distributors:lista_distribuitori')

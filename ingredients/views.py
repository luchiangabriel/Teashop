
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from ingredients.models import Ingredient
from ingredients.forms import EmailForm
from Teashop import settings


class CreateIngredientView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = ['name', 'description', 'quantity', 'distributor']
    template_name = 'ingredients_form.html'

    def get_success_url(self):
        return reverse('ingredients:adauga')


class IngredientsView(ListView):
    model = Ingredient
    template_name = 'ingredients_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Ingredient.objects.filter(active=True)


class UpdateIngredientView(UpdateView):
    model = Ingredient
    fields = ['quantity']
    template_name = 'ingredients_form.html'

    def get_queryset(self):
        return Ingredient.objects.filter(active=True)

    def get_success_url(self):
        return reverse('ingredients:lista_ingrediente')


@login_required
def deactivate_ingredient(request, pk):
    if Ingredient.objects.filter(id=pk).exists:
        Ingredient.objects.filter(id=pk).update(active=False)
    return redirect('ingredients:lista_ingrediente')


@login_required
def prepare_recipe(request, pk):
    if Ingredient.objects.filter(id=pk).exists:
        ingredient = Ingredient.objects.get(id=pk)
        var = ingredient.quantity
        ingredient.update(quantity=var - 1)
    return Ingredient.objects.filter(active=True)


@login_required
def send_mail_s(request):

    message_sent = False

    if request.method == 'POST':

        form = EmailForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = "Quantity Alert"
            message = cd['message']
            send_mail(subject, message,
                      settings.EMAIL_HOST_USER, [cd['recipient']])

            message_sent = True

    else:
        form = EmailForm()

    return render(request, 'send_mail.html', {

        'form': form,
        'message_sent': message_sent,

    })

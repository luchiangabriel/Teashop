
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from recipes.models import Recipe
from ingredients.models import Ingredient


class CreateRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'ingredients', 'image', 'quantity']
    template_name = 'recipes_form.html'

    def get_success_url(self):
        return reverse('recipes:adauga')


class RecipesView(ListView):
    model = Recipe
    template_name = 'recipes_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Recipe.objects.filter(active=True)


class UpdateRecipeView(UpdateView):
    model = Recipe
    fields = ['name', 'ingredients', 'image', 'quantity']
    template_name = 'recipes_form.html'

    def get_queryset(self):
        return Recipe.objects.filter(active=True)

    def get_success_url(self):
        return reverse('recipes:lista_retete')


@login_required()
def updatequantityview(request, pk):
    if Recipe.objects.filter(id=pk).exists():
        recipe_instance = Recipe.objects.get(id=pk)
        ingredient = recipe_instance.quantity
        quantity_diff = recipe_instance.quantity.quantity - 1
        Ingredient.objects.filter(id=ingredient.id).update(quantity=quantity_diff)
    return redirect('recipes:lista_retete')


@login_required
def deactivate_recipe(request, pk):
    if Recipe.objects.filter(id=pk, name=Recipe.name).exists:
        Recipe.objects.filter(id=pk, name=Recipe.name).update(active=False)
    return redirect('recipes:lista_retete')

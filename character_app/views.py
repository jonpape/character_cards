from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Character

class CharacterList(ListView):
    model = Character
    template_name = 'character_list.html'
    context_object_name = 'characters'

class CharacterDetail(DetailView):
    model = Character
    template_name = 'character_detail.html'
    context_object_name = 'character'
    
class CharacterCreate(CreateView):
    model = Character
    template_name = 'character_form.html'
    fields = ['name', 'position', 'department', 'location', \
                'hire_date', 'profile_image', 'lifestyle_image', \
                'character_image', 'superpower', 'skills', \
                'favorite_character', 'motivation', 'quote', 'appreciated_for']
    success_url = reverse_lazy('character_list')

class CharacterUpdate(UpdateView):
    model = Character
    template_name = 'character_update.html'
    fields = ['name', 'position', 'department', 'location', \
                'hire_date', 'profile_image', 'lifestyle_image', \
                'character_image', 'superpower', 'skills', \
                'favorite_character', 'motivation', 'quote', 'appreciated_for']
    success_url = reverse_lazy('character_list')

class RecipeDelete(DeleteView):
    model = Character
    template_name = 'character_confirm_delete.html'
    success_url = reverse_lazy('character_list')



    
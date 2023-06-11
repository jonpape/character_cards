from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Character

def search_results(request):
    query = request.GET.get('q')
    results = Character.objects.filter(name__icontains=query)
    return render(request, 'search_results.html', {'results': results})

class CharacterList(ListView):
    model = Character
    template_name = 'character_list.html'
    context_object_name = 'characters'

class CharacterDetail(DetailView):
    model = Character
    template_name = 'character_detail.html'
    context_object_name = 'character'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('name')
        return queryset
    
class CharacterCreate(CreateView):
    model = Character
    template_name = 'character_form.html'
    fields = ['name', 'position', 'department', 'location', \
                'hire_date', 'profile_image', 'lifestyle_image', \
                'character_image', 'superpower', 'skill_1', 'skill_2', 'skill_3', \
                'favorite_character', 'motivation', 'quote', 'appreciation']
    success_url = reverse_lazy('character_list')

class CharacterUpdate(UpdateView):
    model = Character
    template_name = 'character_update.html'
    fields = ['name', 'position', 'department', 'location', \
                'hire_date', 'profile_image', 'lifestyle_image', \
                'character_image', 'superpower', 'skill_1', 'skill_2', 'skill_3', \
                'favorite_character', 'motivation', 'quote', 'appreciation']
    success_url = reverse_lazy('character_list')

class CharacterDelete(DeleteView):
    model = Character
    template_name = 'character_confirm_delete.html'
    success_url = reverse_lazy('character_list')



    
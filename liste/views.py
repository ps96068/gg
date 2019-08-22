from django.shortcuts import render
from .models import Comanda
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ComandaForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url='/login/')
def home(request):
#    if request.method == 'POST':
#        form = ComandaForm(request.POST or None)
#        if form.is_valid():
#            print(form.cleaned_data)
#    form = ComandaForm()
    liste = Comanda.objects.all()
    paginator = Paginator(liste, 50)
    page = request.GET.get('page')
    liste = paginator.get_page(page)
    #queryset_list = liste
    query = request.GET.get("q")
    if query:
        liste = Comanda.objects.filter(Q(name=query) |
                                       Q(content=query) |
                                       Q(phone=query)
                                    ).distinct()
        reverse_lazy('lista:home')
    return render(request, 'liste/home.html',{'objects_list': liste, })

class ListaDetail(LoginRequiredMixin, DetailView):
    queryset = Comanda.objects.all()
    login_url = '/login/'
    context_object_name = 'object'
    template_name = 'liste/detail.html'


class ListaCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'liste/create.html'
    login_url = '/login/'
    success_url = reverse_lazy('lista:home')
    success_message = 'Ati adaugat o noua comanda'


class ListaUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Comanda
    login_url = '/login/'
    form_class = ComandaForm
    template_name = 'liste/update.html'
    success_url = reverse_lazy('lista:home')
    success_message = 'Ati modificat cu succes comanda'

class ListaDelete(LoginRequiredMixin, DeleteView):
    model = Comanda
    # template_name = 'liste/delete.html'
    login_url = '/login/'
    success_url = reverse_lazy('lista:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Ati sters cu succes comanda')
        return self.post(request, *args, **kwargs)


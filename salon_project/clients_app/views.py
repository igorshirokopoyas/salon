from django.shortcuts import render
from .models import Clients
from django.http import HttpResponse, JsonResponse
import json
from .forms import ClientForm
from django.core import serializers
from .serilizers import ClientsSerilizer
from rest_framework import viewsets

# Create your views here.
def show_records(request):
    all_clients = Clients.objects.all()
    # return HttpResponse('Страница со списком товаров')

    context = {
        'clients': all_clients,
    }

    return render(request, 'show_records.html', context)

def add_client(request):
    form = ClientForm(request.POST or None)
    if request.method == 'POST':
        print(f'form: {form}')
        if form.is_valid():
            form.save()
    # print(request.GET)
    # print(request.POST)
    context = {'form': form}
    return render(request, 'add_client.html', context)

def save_client_data(request):
    if request.method == 'POST':
        try:
            # Получаем данные из POST-запроса
            data = json.loads(request.body)
            # name = request.GET.get('clientName')
            name = data.get('name')
            print(name)
            # return render(request, 'add_client.html')
            return JsonResponse({'success': True})

        except Exception as e:

            print(f'Ошибка при сохранении данных: {e}')

            return JsonResponse({'success': False, 'error': str(e)})

# ---------api------------
class ClientsApi(viewsets.ModelViewSet):
    # http_method_names = ['get']
    queryset = Clients.objects.all()
    serializer_class = ClientsSerilizer
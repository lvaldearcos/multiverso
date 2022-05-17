from django.shortcuts import render, redirect

# Create your views here.
from marvel.models import Personaje


def index(request):
    lista_personajes = Personaje.objects.all()

    return render(request, 'marvel/index.html', {'personajes': lista_personajes})


def crear(request):

    return render(request, 'marvel/crear.html')


def crear_personaje(request):
    if request.method == 'GET':
        return render(request, index)

    else:
        personaje_nuevo = Personaje()
        personaje_nuevo.id = request.POST.get('id')
        personaje_nuevo.img = request.POST.get('img')
        personaje_nuevo.nombre = request.POST.get('nombre')
        personaje_nuevo.poderes = request.POST.get('poderes')
        personaje_nuevo.origen = request.POST.get('origen')

        Personaje.save(personaje_nuevo)

        return redirect(index)


def editar_personaje(request, id):
    if request.method == 'GET':
        personaje = Personaje.objects.get(id=id)
        return render(request, 'marvel/editar.html', {'personaje': personaje})

    else:
        personaje_antiguo = Personaje()
        personaje_antiguo.id = id
        personaje_antiguo.img = request.POST.get('img')
        personaje_antiguo.nombre = request.POST.get('nombre')
        personaje_antiguo.poderes = request.POST.get('poderes')
        personaje_antiguo.origen = request.POST.get('origen')

        Personaje.save(personaje_antiguo)

        return redirect(index)


def borrar_personaje(request, id):
    personaje = Personaje.objects.get(id=id)
    if personaje is not None:
        Personaje.delete(personaje)

    return redirect(index)

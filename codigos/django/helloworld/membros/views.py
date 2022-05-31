from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Membros

def index(request):
    listaMembros = Membros.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'listaMembros': listaMembros,
    }
    return HttpResponse(template.render(context,request))

def adicionar(request):
    template = loader.get_template('adicionar.html')
    return HttpResponse(template.render({},request))

def addmembro(request):
    x = request.POST["nome"]
    y = request.POST["sobrenome"]
    membro = Membros(nome=x,sobrenome=y)
    membro.save()
    return HttpResponseRedirect(reverse('index'))

def apagar(request, id):
  membro = Membros.objects.get(id=id)
  membro.delete()
  return HttpResponseRedirect(reverse('index'))

def editar(request, id):
  membro = Membros.objects.get(id=id)
  template = loader.get_template('editar.html')
  context = {
    'membro': membro,
  }
  return HttpResponse(template.render(context, request))

def editarmembro(request, id):
  nome = request.POST['nome']
  sobrenome = request.POST['sobrenome']
  membro = Membros.objects.get(id=id)
  membro.nome = nome
  membro.sobrenome = sobrenome
  membro.save()
  return HttpResponseRedirect(reverse('index'))

from django.shortcuts import render, get_object_or_404, redirect
from persona.models import Persona, Animal, Consulta, Medicacion, Medicina
from .forms import PersonaForm, AnimalForm, ConsultaForm
from django.contrib import messages

# Create your views here.
def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'persona/lista_personas.html', {'personas':personas})

def detalle_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    return render(request, 'persona/detalle_persona.html',{'persona':persona})

def persona_new(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit = False)
            persona.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()

    return render(request, 'persona/persona_new.html',{'form':form})

def persona_edit(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit = False)
            persona.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
        return render(request, 'persona/persona_new.html',{'form':form})

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'persona/lista_animales.html', {'animales':animales})

def detalle_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'persona/detalle_animal.html',{'animal':animal})

def animal_new(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit = False)
            animal.save()
            return redirect('lista_animales')
    else:
        form = AnimalForm()
    
    return render(request, 'persona/animal_new.html',{'form':form})

def animal_edit(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            animal = form.save(commit = False)
            animal.save()
            return redirect('lista_animales')
    else:
        form = AnimalForm(instance=animal)
        return render(request, 'persona/animal_new.html',{'form':form})


def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'persona/lista_consultas.html', {'consultas':consultas})

def detalle_consulta(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    return render(request, 'persona/detalle_consulta.html',{'consulta':consulta})

def consulta_new(request):
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = Consulta.objects.create(idAnimal=form.cleaned_data['idAnimal'], sintomas=form.cleaned_data['sintomas'], observaciones=form.cleaned_data['observaciones'], diagnostico = form.cleaned_data['diagnostico'], fechaConsulta = form.cleaned_data['fechaConsulta'])
            for medicina_id in request.POST.getlist('receta'):
                medicacion = Medicacion(medicina_id=medicina_id, consulta_id = consulta.id)
                medicacion.save()
            return redirect('lista_consultas')
            
    else:
        form = ConsultaForm()

    return render(request, 'persona/consulta_new.html',{'form':form})

def consulta_edit(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    if request.method == "POST":
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta = form.save(commit = False)
            consulta.save()
            return redirect('lista_consultas')
    else:
        form = ConsultaForm(instance=consulta)
        return render(request, 'persona/consulta_new.html',{'form':form})

    
    
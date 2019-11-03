from django.shortcuts import render, get_object_or_404
from persona.models import Persona
from .forms import PersonaForm

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
            persona.nombre = request.nombre
            persona.apellido = request.apellido
            persona.telefono = request.telefono
            persona.direccion = request.direccion
            persona.save()
            return redirect('detalle_persona', pk=persona.pk)
    else:
        form = PersonaForm()

    return render(request, 'persona/nueva_persona.html',{'form':form})

    
    
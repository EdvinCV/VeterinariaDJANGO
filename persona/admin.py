from django.contrib import admin
from .models import Persona
from .models import TipoAnimal
from .models import Animal

# Register your models here.
admin.site.register(Persona)
admin.site.register(TipoAnimal)
admin.site.register(Animal)

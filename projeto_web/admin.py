from django.contrib import admin

# Register your models here.
from projeto_web.models import Evento,Imagem, Pessoa
from django.contrib import admin

admin.site.register(Evento)
admin.site.register(Imagem)
admin.site.register(Pessoa)

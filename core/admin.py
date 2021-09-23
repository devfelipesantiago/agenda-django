from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "data_evento",
        "data_criacao",
    )  # Campos que devem
    # aparecer no meu evento
    list_filter = (
        "title",
        "usuario",
    )


admin.site.register(Evento, EventoAdmin)

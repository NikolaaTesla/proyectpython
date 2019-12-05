from django.contrib import admin



#importamos cada una de las clases creaddas en el archivo models.py
from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import TipoEstu
from .models import Tipologr

#Agregamos la clase <<Model>>Admin, para modificar la vista a cada 




# Register your models here.

admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(Tipologr)


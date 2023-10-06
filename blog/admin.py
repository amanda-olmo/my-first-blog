from django.contrib import admin

# Register your models here.
from .models import Post

# Para hacer nuestro modelo visible en la pagina del administrador
# tenemos que registrar el modelo con:
admin.site.register(Post)

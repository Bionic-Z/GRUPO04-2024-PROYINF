# app/urls_contenido.py
from django.urls import path
from users.contenido_view import crear_contenido, upload_image
from django.urls import path
from users.contenido_view import editar_contenido
from users.contenido_view import crear_contenido, upload_image, lista_contenido, editar_contenido


urlpatterns = [
    path('crear/', crear_contenido, name='crear_contenido'),  # /contenido/crear/
    path('upload/', upload_image, name='upload_image'),      # /contenido/upload/
    path('lista/', lista_contenido, name='lista_contenido'), # /contenido/lista/
    path('editar/<int:contenido_id>/', editar_contenido, name='editar_contenido'), # /contenido/editar/1/
]


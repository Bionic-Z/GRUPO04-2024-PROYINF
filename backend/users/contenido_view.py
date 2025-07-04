from django.shortcuts import render, redirect
from .models import Contenido
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contenido
from django.urls import reverse
import uuid


def crear_contenido(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        cuerpo = request.POST.get("contenido")
        Contenido.objects.create(titulo=titulo, cuerpo=cuerpo)
        messages.success(request, "Contenido creado exitosamente.")
        return redirect("crear_contenido")
    return render(request, "contenidos/crear_contenido.html")


from django.http import JsonResponse
import os
from django.conf import settings


def upload_image(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        if not image:
            return JsonResponse({"success": 0, "message": "No file uploaded"})

        upload_path = os.path.join(settings.MEDIA_ROOT, "uploads")
        os.makedirs(upload_path, exist_ok=True)

        ext = os.path.splitext(image.name)[1]
        unique_name = f"{uuid.uuid4().hex}{ext}"
        file_path = os.path.join(upload_path, unique_name)

        with open(file_path, "wb+") as f:
            for chunk in image.chunks():
                f.write(chunk)

        image_url = f"{settings.MEDIA_URL}uploads/{unique_name}"
        return JsonResponse({"success": 1, "file": {"url": image_url}})

    return JsonResponse({"success": 0, "message": "Invalid request"})


from django.shortcuts import render
from .models import Contenido


def lista_contenido(request):
    contenidos = Contenido.objects.all().order_by("-creado")
    return render(
        request, "contenidos/lista_contenido.html", {"contenidos": contenidos}
    )


def editar_contenido(request, contenido_id):
    contenido = get_object_or_404(Contenido, id=contenido_id)

    if request.method == "POST":
        contenido.titulo = request.POST.get("titulo")
        contenido.cuerpo = request.POST.get("contenido")
        contenido.save()
        messages.success(request, "Contenido editado exitosamente.")
        return redirect("lista_contenido")

    return render(
        request,
        "contenidos/crear_contenido.html",
        {"contenido": contenido, "editar": True},
    )

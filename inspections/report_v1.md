# Inspección de Código - Hito 5

## Herramienta usada: SonarCloud

Se ejecutó una inspección sobre los módulos críticos del proyecto, identificando problemas de seguridad y confiabilidad.

---

## Issue 1 – Security [E - Blocker]

**Archivo:** `contenido_view.py`  
**Línea afectada:** 31  
**Líneas relacionadas:** 23 y 29  

**Descripción:**  
Uso de ruta construida con datos controlados por el usuario (`image.name`), lo cual puede permitir ataques tipo *path traversal*. Esto ocurre cuando un archivo es guardado usando directamente su nombre original, sin sanitización.

**Captura:**
<p align="center">
  <img src="https://github.com/user-attachments/assets/f4f29c4f-28f1-418d-a006-ab9b3bd7e3d6" width="500" height="150">
</p>
**Recomendación de SonarCloud:**  
Evitar usar directamente rutas derivadas de datos externos. Usar nombres aleatorios o controlados para almacenamiento de archivos.

**Acción tomada:**  
Modificar el código para generar un nombre de archivo aleatorio usando `uuid.uuid4()` y mantener la extensión original. Validar el tipo de archivo antes de guardar.

---

## Issue 2 – Reliability [C - Important]

**Archivo:** `crear_contenido.html`  
**Líneas afectadas:** 3 y 15  

**Descripción:**  
- Línea 3: falta especificar el idioma en el tag `<html>`, lo que puede causar errores de accesibilidad.  
- Línea 15: mal uso del bucle, asignando dentro del mismo, lo que puede llevar a errores lógicos.

**Captura:**

<p align="center">
  <img src="https://github.com/user-attachments/assets/8477a8b9-b3bb-4617-bac2-076ad25e7731" width="500" height="150">
</p>

**Recomendación de SonarCloud:**  
- Declarar `lang="es"` en el documento HTML.
- Refactorizar la lógica del bucle.

**Acción tomada:**  
Actualizar el HTML con `lang="es"` y simplificar el bucle afectado

---

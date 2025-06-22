# Inspección de Código - Hito 5

## Herramienta usada: SonarCloud

Se ejecutó una inspección sobre los módulos críticos del proyecto, identificando problemas de seguridad y confiabilidad.

---

### Resultados de re-inspección con SonarQube

![image](https://github.com/user-attachments/assets/19ed7b3c-9451-401d-a10f-72ebf4bc8a0f)

El nuevo análisis no muestra problemas de ningún nivel en el nuevo código añadido
<p>
  <img src="https://github.com/user-attachments/assets/a66295e0-ab8f-4626-8900-92ad7b2d5f10" weight="250" height="250">
</p>

Sin embargo, en forma general, presenta problemas de seguridad dentro de `contenido_view` a pesar de los cambios

El resultado puede deberse a diversos factores, pero una hipótesis sería que la solución realizada era útil para el problema en el código del momento, por lo que probablemente el código nuevo es equivalente a pesar de ser una solución distinta.

### Commits asociados

- [`0a8958421a816852c41484bece9d264db66b56cc`](https://github.com/Bionic-Z/GRUPO04-2024-PROYINF/commit/0a8958421a816852c41484bece9d264db66b56cc): Add language attribute to HTML tag and adjust heading size for improved accessibility
- [`dc045876c3b563f49e07dd74438b386dd60a3379`](https://github.com/Bionic-Z/GRUPO04-2024-PROYINF/commit/dc045876c3b563f49e07dd74438b386dd60a3379): Refactor image upload logic to use unique filenames and clean up imports

- ---

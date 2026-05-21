# 🚀 Mi Viaje de Aprendizaje con Django y Git: Hacia mi Portafolio Profesional

¡Bienvenido/a a este repositorio! Este proyecto no es una página web estática ni un ejercicio terminado; **es un espacio en constante evolución**. Mi objetivo es transformar este código inicial, paso a paso, en mi **portafolio profesional definitivo**. 

La idea central de este repositorio es la **transparencia y la mejora continua**: quiero que cualquier persona que entre aquí pueda ver el historial de cambios, notar en qué me equivoqué, cómo enfrenté los desafíos técnicos y de qué manera fui refinando el código hasta construir una aplicación robusta, moderna y eficiente. ¡El camino del aprendizaje es lo que realmente da valor al resultado final!

---

## 🛠️ Tecnologías y Conceptos Practicados
* **Backend:** Python 3, Django (MVT, URLconf, Views, Context Data).
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Cards, Carousels, Badges, Responsive Design).
* **Control de Versiones:** Git & GitHub.

---

## 🧠 Lo Que Aprendí Hoy (Conceptos Dominados)
Hoy dominé las cuatro herramientas esenciales del sistema de plantillas de Django (**DTL**):
1. **`{% include %}`:** A modularizar código para reutilizar componentes como barras de navegación (`navbar.html`) y pies de página (`footer.html`), manteniendo un proyecto limpio (**DRY** - *Don't Repeat Yourself*).
2. **`{{ variables }}`:** A pasar datos dinámicos estructurados en diccionarios de Python desde la vista (`views.py`) y renderizarlos limpiamente en el HTML.
3. **`{% for %}`:** A iterar listas de datos (como tareas y artículos de blog) y generar estructuras visuales repetitivas automáticamente usando `{{ forloop.counter }}` para enumerar elementos.
4. **`{% if %}`:** A implementar lógica condicional en el frontend para cambiar dinámicamente clases de Bootstrap (como insignias de estados `bg-success` y `bg-warning`).

---

## 📈 Lo Que Mejoré
* **Comprensión de la Arquitectura Web:** Entendí el flujo de una petición en Django (Petición ➡️ URLconf ➡️ Vista ➡️ Template) y por qué es una mala práctica saturar las vistas con lógica pesada (*"Modelos gordos, Vistas flacas"*).
* **Diseño UI Responsivo:** Mejoré la presentación visual de la información utilizando componentes avanzados de Bootstrap, como carruseles de imágenes de hardware/tecnología y tarjetas con sombras estilizadas.
* **Manejo de la Terminal y Git:** Gané soltura administrando repositorios locales y configurando conexiones con repositorios remotos.

---

## ⚠️ Lo Que Me Equivoqué (Y Cómo lo Solucioné)
El error es parte fundamental del crecimiento técnico. Estos fueron mis principales tropezones de hoy:

1. **El Clásico Error 404 (URL Inexistente):**
   * *Qué pasó:* Intenté acceder a `productos1/` en el navegador y Django arrojó un error detallado de rutas.
   * *Qué aprendí:* Comprendí la rigurosidad del archivo `urls.py`. Aprendí a leer el mapa de rutas que Django genera con `DEBUG = True` para identificar errores de tipeo o rutas no registradas rápidamente.
2. **Sintaxis Incorrecta en Git Remote:**
   * *Qué pasó:* Al intentar desvincular un repositorio remoto, ejecuté `git remote remove` sin especificar el alias.
   * *Qué aprendí:* Revisé la documentación de comandos de Git. Aprendí a usar `git remote -v` para listar y verificar el nombre exacto del enlace remoto (que comúnmente es `origin`) antes de intentar eliminarlo.
3. **Paso Directo de Contexto en Render:**
   * *Qué pasó:* Inicialmente pasé un diccionario de datos plano directamente en el argumento de contexto de la función `render()`.
   * *Qué aprendí:* Comprendí que la mejor práctica es envolver los datos dentro de un diccionario de contexto estructurado (ej. `context = {'usuario': datos_usuario}`) para mantener el código escalable y ordenado al renderizar en el template.

---

## 🚀 Próximos Pasos (Hacia la Mejora Continua)
* [ ] Conectar la aplicación a una Base de Datos real mediante los **Modelos de Django (`models.py`)**.
* [ ] Crear formularios dinámicos para que el usuario pueda agregar nuevas tareas o artículos desde la interfaz web.
* [ ] Implementar el sistema de autenticación de usuarios propio de Django.

---
*«El código limpio no es el que se escribe perfecto a la primera, sino el que se refina constantemente a través del aprendizaje diario.»*

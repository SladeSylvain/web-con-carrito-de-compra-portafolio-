# 🚀 Portafolio Web con Django — Diario de Aprendizaje

Bienvenido/a a este repositorio. No es un proyecto terminado: **es un portafolio en construcción constante**. Cada commit representa un día real de estudio, errores, soluciones y conceptos nuevos dominados. Si entras aquí, verás exactamente cómo pasé de una página HTML estática a una aplicación Django con autenticación, permisos y base de datos.

---

## 🛠️ Stack Tecnológico

| Capa | Tecnologías |
|---|---|
| **Backend** | Python 3, Django (MVT, ORM, Forms, Auth) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Base de Datos** | SQLite (desarrollo) |
| **Control de Versiones** | Git & GitHub |

---

## 📁 Estructura del Proyecto

```
config/           → Configuración global (settings.py, urls.py)
myfirstapp/
  ├── models.py   → Modelos: Tarea, Contacto, Usuario
  ├── views.py    → Vistas con lógica y permisos
  ├── forms.py    → Formularios con validación
  ├── admin.py    → Panel de administración
  ├── templates/  → HTML con Django Template Language
  └── static/     → Imágenes y recursos estáticos
```

---

## 📅 Historial de Aprendizaje (Día a Día)

### Día 1 — 19 May · *Página web base*
`f529a96`

El punto de partida. Proyecto Django creado desde cero: configuración inicial, primera app (`myfirstapp`) y servidor corriendo localmente.

**Conceptos activados:** `django-admin startproject`, `startapp`, `runserver`, estructura de carpetas de Django.

---

### Día 2 — 20 May · *Portafolio con carrito de compra + README + Mejora de perfil*
`3b0ec7a` · `7159418` · `22a0443`

El salto grande inicial. Se construyeron las primeras páginas reales del portafolio usando el sistema de plantillas de Django (DTL) y componentes de Bootstrap 5.

**Lo que se construyó:**
- Páginas: `home`, `perfil`, `presentacion`, `contacto`, `productos` (3 variantes)
- Componentes reutilizables: `navbar.html` y `footer.html` con `{% include %}`
- Datos dinámicos pasados desde `views.py` al template con `{{ variables }}`
- Iteración de listas con `{% for %}` y `{{ forloop.counter }}`
- Lógica condicional con `{% if %}` para cambiar clases de Bootstrap (badges `bg-success` / `bg-warning`)
- Banner de imagen estática registrado en `settings.py`

**Errores que enfrenté:**
- **Error 404:** Intenté acceder a `productos1/` sin registrar la ruta. Aprendí a leer el mapa de URLs que Django genera con `DEBUG = True`.
- **Contexto mal estructurado:** Pasé datos planos directo al `render()` en vez de envolverlos en un diccionario. Solución: `context = {'clave': valor}`.

**Conceptos dominados:** `{% include %}`, `{{ variables }}`, `{% for %}`, `{% if %}`, flujo Petición → URLconf → Vista → Template, principio DRY.

---

### Día 3 — 23 May · *Admin, Formulario de Registro + Ramas Git*
`6370d60` · `e870779` · `fbd1c8c` · `ef64aa2` · `ede071b`

Día intenso: dos temas al mismo tiempo. Por un lado, conectar Django con el panel de administración y crear el primer formulario real. Por otro, aprender a trabajar con ramas en Git.

**Lo que se construyó:**
- `admin.py` configurado para gestionar modelos desde el panel `/admin`
- Modelo `Usuario` con campos: `username`, `email`, `edad`, `ciudad`, `password`
- Formulario de registro (`RegistroForm`) con `ModelForm`
- Primera migración `0001_initial.py` y base de datos SQLite activa
- Página `registro.html` conectada a la vista con lógica POST/GET

**Git — lo que practiqué:**
- Crear y cambiar ramas: `git branch pruebas1`, `git switch`
- Combinar cambios: `git merge`
- Resolver un merge con repositorio remoto: `git pull` + resolución de conflicto

**Errores que enfrenté:**
- **`git remote remove` sin alias:** Ejecuté el comando incompleto. Solución: usar `git remote -v` primero para ver el nombre exacto (`origin`).
- Conflicto de merge entre rama local y remota: aprendí a leer el diff y aceptar los cambios correctos.

**Conceptos dominados:** `ModelForm`, `migrations`, panel `admin`, `git branch`, `git merge`, resolución de conflictos.

---

### Día 4 — 25 May · *Modelo Tarea + Posts en Admin*
`b172088`

Se añadió el modelo `Tarea` y se registró en el panel de administración. También se conectó el formulario de contacto al ORM para persistir mensajes en la base de datos.

**Lo que se construyó:**
- Modelo `Tarea`: campos `titulo` (CharField), `completada` (BooleanField), `creada` (DateTimeField auto)
- Modelo `Contacto`: campos `name`, `email`, `message`
- `admin.py` actualizado con ambos modelos visibles en `/admin`
- Migración `0002_tarea.py`
- Vista `contacto` actualizada para leer y mostrar los contactos guardados con `Contacto.objects.all()`

**Conceptos dominados:** `BooleanField`, `DateTimeField(auto_now_add=True)`, `objects.all()`, registro de múltiples modelos en `admin.py`.

---

### Día 5 — 27 May · *Sistema de Permisos y Seguridad*
`fa27a10`

El salto cualitativo más grande hasta ahora. Se implementó un sistema real de control de acceso usando el módulo de autenticación nativo de Django.

**Lo que se construyó:**
- `@login_required` en vistas protegidas (redirige a login si no hay sesión activa)
- `request.user.has_perm('myfirstapp.add_contacto')` para controlar quién puede enviar mensajes
- `PermissionDenied` como excepción HTTP cuando un usuario intenta una acción no autorizada
- Vista `borrar_contacto` con verificación doble de permisos (`delete_contacto` o `add_contacto`)
- Sistema de mensajes (`messages.warning`) combinado con alertas Bootstrap
- Confirmación JS con `onclick="return confirm(...)"` para evitar borrados accidentales
- Contraseña encriptada con `make_password()` al registrar usuarios
- Validación personalizada `clean_password()` en el formulario (mínimo 6 caracteres)
- Migración `0003_usuario_password.py`
- Renderizado condicional en templates con `{% if perms %}` para ocultar elementos según el rol

**Errores que enfrenté:**
- Entender la diferencia entre ocultar un botón en el template (UX) y bloquear la ruta en el servidor (seguridad real). Ambos son necesarios.

**Conceptos dominados:** `@login_required`, `@permission_required`, `has_perm()`, `PermissionDenied`, `messages`, `make_password()`, validaciones `clean_<field>()`, seguridad en frontend Y backend.

---

## 🧠 Resumen de Conceptos Acumulados

```
Django Template Language    ✅  {% include %}, {{ var }}, {% for %}, {% if %}, {% if perms %}
ORM & Modelos               ✅  CharField, EmailField, BooleanField, DateTimeField, ForeignKey (próximo)
Formularios                 ✅  ModelForm, widgets, clean_field(), validaciones personalizadas
Autenticación               ✅  login_required, has_perm(), PermissionDenied, make_password()
Panel Admin                 ✅  Registro de modelos, gestión visual desde /admin
Migraciones                 ✅  makemigrations, migrate, historial de esquema
Git                         ✅  commit, push, pull, branch, switch, merge, resolución de conflictos
Bootstrap 5                 ✅  Cards, Carousels, Badges, Alerts, Responsive Grid
```

---

## 🔜 Próximos Pasos

- [ ] Migrar el modelo `Usuario` al sistema `AbstractUser` de Django para integrar autenticación nativa completa
- [ ] Implementar CRUD completo para tareas (crear, editar, eliminar desde el frontend)
- [ ] Añadir paginación a las listas de contactos y tareas
- [ ] Configurar variables de entorno con `python-decouple` (sacar `SECRET_KEY` del código)
- [ ] Deploy en Railway o Render

---

## ▶️ Correr el Proyecto Localmente

```bash
git clone https://github.com/SladeSylvain/web-con-carrito-de-compra-portafolio-
cd "django 1.5"
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Luego entra a `http://127.0.0.1:8000/` y al panel de admin en `http://127.0.0.1:8000/admin/`.

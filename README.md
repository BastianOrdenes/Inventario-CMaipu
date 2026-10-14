# Sistema Comercial Maipú

Este repositorio contiene el sistema completo de Comercial Maipú desarrollado en Django y MySQL:

1. **Plataforma Web (Evaluación 2):** Vistas tradicionales con plantillas HTML y Bootstrap.
2. **API RESTful (Evaluación 3):** Endpoints con Django REST Framework, autenticación SimpleJWT, manejo de imágenes y archivos de prueba.

## Pasos para ejecutar

1. Instalar dependencias:
   pip install -r requirements.txt

2. Configurar credenciales de MySQL en `settings.py`

3. Aplicar migraciones:
   python manage.py migrate

4. Crear superusuario:
   python manage.py createsuperuser

5. Iniciar servidor:
   python manage.py runserver

## Recursos para la Evaluación 3 (API REST)
* **Colección de Bruno:** Carpeta `inventariocomercialmaipuAPI/`
* **Imágenes de prueba para POST:** Carpeta `fotosmuebles_test/`
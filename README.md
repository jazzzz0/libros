# 📚 Sistema de Biblioteca - Django

Sistema de gestión de biblioteca desarrollado con Django para administrar autores y libros.
Actividad de la materia de Desarrollo de Sistemas Web.

## 🚀 Características

- Gestión de autores (nombre y nacionalidad)
- Gestión de libros (título, resumen y autor)
- Panel de administración web con funcionalidades avanzadas de búsqueda y filtrado
- Búsqueda de autores por nombre y nacionalidad
- Búsqueda de libros por título y nombre del autor
- Filtrado de libros por autor

## 📥 Clonar el repositorio

```bash
git clone https://github.com/jazzzz0/libros.git
cd libros
```

## 🏃‍♂️ Ejecutar el proyecto

1. **Crear entorno virtual**
   ```bash
   python -m venv env
   ```

2. **Activar entorno virtual**
   ```bash
   # Windows
   .\env\Scripts\activate
   
   # Linux/Mac
   source env/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar servidor**
   ```bash
   python manage.py runserver
   ```

7. **Abrir en navegador**
   - http://localhost:8000/index/ - Página principal
   - http://localhost:8000/admin/ - Panel de administración
   - http://localhost:8000/libros/ - Lista estática de libros
   - http://localhost:8000/autores/ - Lista de autores registrados a través del panel de administración

## 📖 Instrucciones de Uso

### Panel de Administración

Una vez que hayas creado el superusuario y encendido el servidor, puedes acceder al panel de administración en `/admin/` para gestionar:

#### 👨‍💼 **Author (Autor)**
- **Crear autor**: Click en "Authors" → "Add author"
- **Campos requeridos**: Nombre (máximo 80 caracteres)
- **Campos opcionales**: Nacionalidad (máximo 100 caracteres)
- **Editar/Eliminar**: Usar los botones de acción en la lista

#### 📚 **Book (Libro)**
- **Crear libro**: Click en "Books" → "Add book"
- **Campos requeridos**: Título (máximo 150 caracteres) y Autor
- **Campos opcionales**: Resumen (texto largo)
- **Relación**: Seleccionar un autor existente de la lista desplegable
- **Editar/Eliminar**: Usar los botones de acción en la lista

**Nota**: Para crear un libro, primero debes tener al menos un autor creado.

### 🔍 Funcionalidades de Búsqueda y Filtrado

El panel de administración incluye capacidades avanzadas para encontrar y organizar la información:

#### 📝 **Búsqueda de Autores**
- **Por nombre**: Busca autores escribiendo parte de su nombre
- **Por nacionalidad**: Filtra autores por país de origen
- **Búsqueda combinada**: Ambos campos son buscables simultáneamente

#### 📚 **Búsqueda de Libros**
- **Por título**: Encuentra libros escribiendo parte del título
- **Por autor**: Busca libros por el nombre del autor asociado
- **Búsqueda inteligente**: La búsqueda funciona con coincidencias parciales

#### 🎯 **Filtrado de Libros**
- **Filtro por autor**: Muestra solo los libros de un autor específico
- **Vista organizada**: Los libros se agrupan por autor para facilitar la navegación
- **Filtros combinables**: Puedes combinar búsquedas con filtros para resultados más precisos

**Nota**: Utiliza la barra de búsqueda en la parte superior de cada lista para encontrar rápidamente el contenido que necesitas.

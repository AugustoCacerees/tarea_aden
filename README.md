# Módulo de Odoo - Gestión de Alumnos e Inscripciones a Programas
Este repositorio contiene un módulo personalizado de Odoo versión 15 diseñado para gestionar alumnos y sus inscripciones a programas educativos. El módulo proporciona las siguientes características: 

## Modelos de Datos
### Modelo Alumno
* Nombre
* Apellido
* Fecha de nacimiento
* Número de legajo
* Email
* Teléfono
* Dirección
* País de origen
### Modelo Programa
* Nombre
* Descripción
### Modelo Inscripción
Permite registrar la inscripción de un alumno a un programa específico.

## Funcionalidad Destacada
El módulo incluye una función especial en el modelo Programa que permite obtener una lista de todos los alumnos inscritos en un programa dado. La función toma como parámetro un programa y devuelve una lista de diccionarios con información detallada de los alumnos inscritos, incluyendo:
* Nombre
* Apellido
* Fecha de nacimiento
* Número de legajo
* Email
* Teléfono
* País de origen

 ## Autor
Augusto Caceres

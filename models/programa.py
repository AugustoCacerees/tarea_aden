from odoo import api, fields, models, _, tools

class Programa(models.Model):
    _name = 'modulo_alumnos.programa'
    _description = 'Modelo Programa'
    _rec_name = 'nombre'

    #Atributos
    nombre = fields.Char(string='Nombre') #Tiene una longitud maxima de 50 caracteres
    descripcion = fields.Text(string='Descripcion')

    #Funcion
    def get_alumnos_inscritos(self, programa_id):
        inscripciones = self.env['modulo_alumnos.incripcion'].search([('programa_id', '=', programa_id)])
                     #env: permite acceso a los modelos y registros de la base de datos.
                     #search: campo "programa_id" coincide con el ID del programa actual (self.id).

        alumnos = inscripciones.mapped('alumnos_id')
                      #mapped: devuelve una lista con los IDs de alumnos (relacionados a través del campo alumno_id) en
                      #       esas inscripciones. Devuelve objetos
        resp_alumnos = []

        for alumno in alumnos:
            resp_alumnos.append({
            'nombre': alumno.nombre,
            'apellido': alumno.apellido,
            'legajo': alumno.legajo,
            'fecha_nacimiento': alumno.fecha_nacimiento,
            'email': alumno.email,
            'telefono': alumno.telefono,
            'pais': {
                'id': alumno.pais.id,
                'nombre': alumno.pais.name,
            }})

        return resp_alumnos
from odoo import api, fields, models, _, tools

class Programa(models.Model):
    _name = 'modulo_alumnos.programa'
    _description = 'Modelo Programa'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripcion')

    def get_alumnos_inscritos(self, programa_id):
        inscripciones = self.env['modulo_alumnos.incripcion'].search([('programa_id', '=', programa_id)])
        alumnos = inscripciones.mapped('alumnos_id')
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
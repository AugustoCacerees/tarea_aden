from odoo import api, fields, models, _, tools

class Inscripcion(models.Model):
    _name = 'modulo_alumnos.inscripcion'
    _description = 'Modulo Descripcion'

    #Atributos
    alumnos_id = fields.Many2one('modulo_alumnos.alumno', string='Alumno')
    programa_id = fields.Many2one('modulo_alumnos.programa', string='Programa')


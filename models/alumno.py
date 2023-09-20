from odoo import api, fields, models, _, tools

class Alumno(models.Model):
    _name = 'modulo_alumnos.alumno'
    _description = 'Modelo Alumno'
    _rec_name='nombre'

    #Atributos
    nombre = fields.Char(string='Nombre')
    apellido = fields.Char(string='Apellido')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    legajo = fields.Integer(string='Numero Legajo')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Telefono')
    direccion = fields.Char(string='Direccion')
    pais = fields.Many2one('res.country', string='País')

    #Many2one:
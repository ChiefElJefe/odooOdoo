from odoo import models, fields, api, exceptions


class Car(models.Model):
    # Nombre del modulo
    _name = 'odoo_model_advanced.car'
    _description = 'Coche'
    # Name es obligatorio
    name = fields.Char(string='Modelo')
    number_plate = fields.Char(string='Matrícula')
    cv = fields.Float(string='CV')
    colour = fields.Char(string='Color')
    fuel_litres = fields.Float(string='Litros')
    new = fields.Boolean(string="Aceptar")
    selectionCar = fields.Selection([('Coche de trabajo', 'Coche de trabajo'), ('Coche particular', 'Coche particular'),
                                     ('Coche de alquiler', 'Coche de alquiler')])
    description = fields.Text(string="Descripción: ")
    img = fields.Binary(string="Coche", help="Seleccionar imagen")


class Marca(models.Model):
    _name = 'odoo_model_advanced.marca'
    _description = 'Marca'

    name = fields.Char(string="Marca")

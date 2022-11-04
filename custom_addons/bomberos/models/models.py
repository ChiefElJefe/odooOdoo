# -*- coding: utf-8 -*-

from odoo import models, fields, api


class parque(models.Model):
    _name = 'parque.bomberos'
    _description = 'parque.bomberos'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Integer(string='Codigo del Parque', required=True)
    descripcion = fields.Text(string='Descripción')
    direccion = fields.Char(string='Dirección')
    plazas = fields.Selection([('2', '2'), ('5', '5'), ('10', '10')], string="Plazas")

    camion_id = fields.One2many('camion.bomberos', 'parque_id', string='Camión')


class camion(models.Model):
    _name = 'camion.bomberos'
    _descripcion = 'camion.bomberos'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Integer(string='Codigo de Camión', required=True)
    marca = fields.Char(string='Marca')
    fecha_compra = fields.Date(string='Fecha de compra')
    descripcion = fields.Text(string="Descripción")

    bombero_id = fields.One2many('bombero.bomberos', 'camion_id', string='Bomberos')
    parque_id = fields.Many2one('parque.bomberos', string='Parque')


class bombero(models.Model):
    _name = 'bombero.bomberos'
    _description = 'bombero.bomberos'

    name = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad")
    foto = fields.Image(string="Foto")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    sexo = fields.Selection([('Hombre', 'Hombre'), ('Mujer', 'Mujer')], string="Sexo")
    descripcion = fields.Text(string="Descripción")

    camion_id = fields.Many2one('camion.bomberos', string='Camion')

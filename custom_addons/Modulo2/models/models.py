# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libro(models.Model):
    _name = 'modulo2.libro'
    _description = 'Libros'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

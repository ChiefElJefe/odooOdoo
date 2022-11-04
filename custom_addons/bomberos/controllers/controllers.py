# -*- coding: utf-8 -*-
# from odoo import http


# class Bomberos(http.Controller):
#     @http.route('/bomberos/bomberos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bomberos/bomberos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bomberos.listing', {
#             'root': '/bomberos/bomberos',
#             'objects': http.request.env['bomberos.bomberos'].search([]),
#         })

#     @http.route('/bomberos/bomberos/objects/<model("bomberos.bomberos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bomberos.object', {
#             'object': obj
#         })

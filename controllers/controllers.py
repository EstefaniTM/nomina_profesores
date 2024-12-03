# -*- coding: utf-8 -*-
# from odoo import http


# class NominaProfesores(http.Controller):
#     @http.route('/nomina_profesores/nomina_profesores', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nomina_profesores/nomina_profesores/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nomina_profesores.listing', {
#             'root': '/nomina_profesores/nomina_profesores',
#             'objects': http.request.env['nomina_profesores.nomina_profesores'].search([]),
#         })

#     @http.route('/nomina_profesores/nomina_profesores/objects/<model("nomina_profesores.nomina_profesores"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nomina_profesores.object', {
#             'object': obj
#         })


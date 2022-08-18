# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleCra(http.Controller):
#     @http.route('/module_cra/module_cra', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_cra/module_cra/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_cra.listing', {
#             'root': '/module_cra/module_cra',
#             'objects': http.request.env['module_cra.module_cra'].search([]),
#         })

#     @http.route('/module_cra/module_cra/objects/<model("module_cra.module_cra"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_cra.object', {
#             'object': obj
#         })

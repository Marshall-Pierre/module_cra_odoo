# -*- coding: utf-8 -*-
from odoo import http


class CraDev(http.Controller):
    @http.route('/cra_dev/cra_dev', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('cra_dev.index')

#     @http.route('/cra_dev/cra_dev/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cra_dev.listing', {
#             'root': '/cra_dev/cra_dev',
#             'objects': http.request.env['cra_dev.cra_dev'].search([]),
#         })

#     @http.route('/cra_dev/cra_dev/objects/<model("cra_dev.cra_dev"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cra_dev.object', {
#             'object': obj
#         })

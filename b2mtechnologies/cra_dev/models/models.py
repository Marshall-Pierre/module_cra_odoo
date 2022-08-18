# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cra_dev(models.Model):
    _name = 'cra_dev.cra_dev'
    # _description = 'cra_dev.cra_dev'

    name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

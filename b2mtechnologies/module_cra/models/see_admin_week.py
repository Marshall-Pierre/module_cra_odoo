from odoo import api, fields, models

class WeekAdminModel(models.Model):
    _name = "week.amin.model"
    _description = "Semaine de la charge acutel des project"

    name = fields.Char(string="Semaine du")
    week_id = fields.Many2one("week.model")

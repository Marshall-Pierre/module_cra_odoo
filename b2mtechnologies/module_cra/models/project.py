from odoo import fields, models

class ProjectModel(models.Model):
    _name = "project.model"
    _description = "Liste des projets"

    name = fields.Char(required=True)
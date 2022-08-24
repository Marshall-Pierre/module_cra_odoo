from typing_extensions import Required
from odoo import fields, models

class ProjectModel(models.Model):
    _name = "project.model"
    _description = "Liste des projets"

    project_manager_id = fields.Many2one("res.users", string="Chargé de project", default=lambda self: self.env.user, readonly=True)
    name = fields.Char(required=True, string="Nom du projet")
    task_ids = fields.One2many("task.model","id", string="Tâches du projet")
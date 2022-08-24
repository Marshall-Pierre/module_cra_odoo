from odoo import api, fields, models

class TaskModel(models.Model):
    _name = "task.model"
    _description = "tâches relative a un projet"

    name = fields.Char(required = True, string="Nom de la tâche")
    project_implementer_ids = fields.Many2many("res.users", string="Exécuatnt du projet")
    load = fields.Integer(required = True, string="Charge de la tâche")
    project_id = fields.Many2one("project.model", "id", default=lambda self: self.project_id)

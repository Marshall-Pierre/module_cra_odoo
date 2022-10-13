from odoo import api, fields, models

class TaskModel(models.Model):
    _name = "task.model"
    _description = "tâches relative a un projet"

    def _get_default_Project_id(self):
        return self.env['project.model'].search([]).name

    name = fields.Char(required = True, string="Nom de la tâche")
    project_implementer_ids = fields.Many2many("res.users", string="Exécuatnt du projet")
    load_task = fields.Integer(required = True, string="Charge de la tâche")
    project_id = fields.Many2one("project.model", required=True, default=_get_default_Project_id)

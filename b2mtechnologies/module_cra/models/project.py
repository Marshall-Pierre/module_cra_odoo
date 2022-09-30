from email.policy import default
from typing_extensions import Required
from odoo import api, fields, models

class ProjectModel(models.Model):
    _name = "project.model"
    _description = "Liste des projets"

    project_manager_id = fields.Many2one("res.users", string="Chargé de project", default=lambda self: self.env.user, readonly=True)
    name = fields.Char(required=True, string="Nom du projet")
    task_ids = fields.One2many("task.model", "project_id", string="Tâches du projet")
    total_load = fields.Float(compute="_compute_total_load", readonly=True, string="Charge total du projet")

    @api.depends("task_ids")
    def _compute_total_load(self):
        for element in self:
            if not element.task_ids:
                element.total_load = 0
            else:
                for load_task in element.task_ids:
                    element.total_load += load_task.load_task


    # total_load = fields.Char(compute="_compute_total_load")

    # @api.depends("task_ids")
    # def _compute_total_load(self):
    #     numnull = 0
    #     for element in self:
    #         for i in range(0, len(element.task_ids)):
    #             element.total_load = numnull + element.task_ids.load_task[i]
    #             numnull = element.total_load
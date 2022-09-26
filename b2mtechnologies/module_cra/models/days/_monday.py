from odoo import api, fields, models

class MondayModel(models.Model):
    _name = "monday.model"
    _description = "Information relative aux lundi"

    name = fields.Float(compute="_compute_total_load")
    date = fields.Date()
    task_id0 = fields.Many2one("task.model")
    task_id1 = fields.Many2one("task.model")
    task_id2 = fields.Many2one("task.model")
    task_id3 = fields.Many2one("task.model")

    load_task0 = fields.Float()
    load_task1 = fields.Float()
    load_task2 = fields.Float()
    load_task3 = fields.Float()


    @api.depends("load_task0", "load_task1", "load_task2", "load_task3")
    def _compute_total_load(self):
        for element in self:
            element.name = element.load_task0 + element.load_task1 + element.load_task2 + element.load_task3
from odoo import fields, models

class WednesdayModel(models.Model):
    _name = "wednesday.model"
    _description = "Information relative aux mercredi"

    name = fields.Char(string="Mercredi")
    date = fields.Date()
    task_id0 = fields.Many2one("task.model")
    task_id1 = fields.Many2one("task.model")
    task_id2 = fields.Many2one("task.model")
    task_id3 = fields.Many2one("task.model")

    load_task0 = fields.Float()
    load_task1 = fields.Float()
    load_task2 = fields.Float()
    load_task3 = fields.Float()
from odoo import fields, models

class FridayModel(models.Model):
    _name = "friday.model"
    _description = "Information relative aux vendredi"

    name = fields.Char(string="Vendredi")
    date = fields.Date()
    task_id0 = fields.Many2one("task.model")
    task_id1 = fields.Many2one("task.model")
    task_id2 = fields.Many2one("task.model")
    task_id3 = fields.Many2one("task.model")

    load_task0 = fields.Float()
    load_task1 = fields.Float()
    load_task2 = fields.Float()
    load_task3 = fields.Float()
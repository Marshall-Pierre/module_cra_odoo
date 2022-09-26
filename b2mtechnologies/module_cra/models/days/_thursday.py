from odoo import fields, models

class ThursdayModel(models.Model):
    _name = "thursday.model"
    _description = "Information relative aux jeudi"

    name = fields.Char(string="Jeudi")
    date = fields.Date()
    task_id0 = fields.Many2one("task.model")
    task_id1 = fields.Many2one("task.model")
    task_id2 = fields.Many2one("task.model")
    task_id3 = fields.Many2one("task.model")

    load_task0 = fields.Float()
    load_task1 = fields.Float()
    load_task2 = fields.Float()
    load_task3 = fields.Float()
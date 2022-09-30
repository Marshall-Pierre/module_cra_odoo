from xml.dom import ValidationErr
from odoo import api, fields, models

class MondayModel(models.Model):
    _name = "monday.model"
    _description = "Information relative aux lundi"

    name = fields.Float(compute="_compute_total_load", string="Charge")
    date = fields.Date()
    task_id0 = fields.Many2one("task.model", string="Tâche n°1")
    task_id1 = fields.Many2one("task.model", string="Tâche n°2")
    task_id2 = fields.Many2one("task.model", string="Tâche n°3")
    task_id3 = fields.Many2one("task.model", string="Tâche n°4")

    load_task0 = fields.Float(string="Charge")
    load_task1 = fields.Float(string="Charge")
    load_task2 = fields.Float(string="Charge")
    load_task3 = fields.Float(string="Charge")

    comment_task0 = fields.Text(string="Commentaire")
    comment_task1 = fields.Text(string="Commentaire")
    comment_task2 = fields.Text(string="Commentaire")
    comment_task3 = fields.Text(string="Commentaire")


    @api.depends("load_task0", "load_task1", "load_task2", "load_task3")
    def _compute_total_load(self):
        for element in self:
            element.name = element.load_task0 + element.load_task1 + element.load_task2 + element.load_task3

    @api.onchange('load_task0', 'load_task1', 'load_task2', 'load_task3')
    def _onchange_price(self):
        # set auto-changing field
        # self.price = self.amount * self.unit_price
        # Can optionally return a warning and domains
        if self.load_task0 > 1:
            self.load_task0 = 1
            return {
                'warning': {
                    'title': "Valeur non valide",
                    'message': "Veuillez entrer une valeur égale ou inférieure à 1",
                }
            }


    # @api.constrains('load_task0', 'load_task1', 'load_task2', 'load_task3')
    # def _check_something(self):
    #     for record in self:
    #         if record.load_task0 > 1:
    #             raise {
    #                     'warning': {
    #                         'title': "Something bad happened",
    #                         'message': "It was very bad indeed",
    #                     }
    #                 }
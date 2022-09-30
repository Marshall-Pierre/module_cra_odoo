from odoo import api, fields, models

class WeekModel(models.Model):
    _name = "week.model"
    _description = "Semaine de la charge acutel des project"

    name = fields.Char(string="Semaine du")
    user_id = fields.Many2one("res.users", string="Chargé de semaine", default=lambda self: self.env.user, readonly=True)
    monday_id = fields.Many2one("monday.model", string="Lundi")
    tuesday_id = fields.Many2one("tuesday.model")
    wednesday_id = fields.Many2one("wednesday.model")
    thursday_id = fields.Many2one("thursday.model")
    friday_id = fields.Many2one("friday.model")

    # id_utilisateur = fields.Integer(default=lambda self: self.env.user._uid)

    # @api.depends("user_id")
    # def init(self):
    #     self._cr.execute("""SELECT * FROM module_cradb_dev where user_id = 'user_id'""")

    # search_ids = fields.Char(compute="_compute_search_ids",search='search_ids_search')

    # @api.depends("user_id")
    # def _compute_search_ids(self):
    #     print('my compute')

    # def search_ids_search(self, operator, operant):
    #     obj = self.env['week.model'].search([('user_id', '=',self.env.user.user_id.id)]).ids
    #     return [('id','in',obj)]

    # lundi = fields.Char(string="Lundi")
    # task_monday0 = fields.Many2one("task.model")
    # task_monday1 = fields.Many2one("task.model")
    # task_monday2 = fields.Many2one("task.model")
    # task_monday3 = fields.Many2one("task.model")
    # load_task_monday0 = fields.Integer()
    # load_task_monday1 = fields.Integer()
    # load_task_monday2 = fields.Integer()
    # load_task_monday3 = fields.Integer()


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
    load_week = fields.Float(compute="_compute_load_week", readonly=True, string="Charge de la semaine", default=0)

    @api.depends("monday_id", "tuesday_id", "wednesday_id", "thursday_id", "friday_id")
    def _compute_load_week(self):
        for element in self:
            if not element.monday_id:
                None
            else:
                element.load_week = element.monday_id.load_task0 + element.monday_id.load_task1 + element.monday_id.load_task2 + element.monday_id.load_task3 + element.load_week

            if not element.tuesday_id:
                None
            else:
                element.load_week = element.tuesday_id.load_task0 + element.tuesday_id.load_task1 + element.tuesday_id.load_task2 + element.tuesday_id.load_task3 + element.load_week

            if not element.wednesday_id:
                None
            else:
                element.load_week = element.wednesday_id.load_task0 + element.wednesday_id.load_task1 + element.wednesday_id.load_task2 + element.wednesday_id.load_task3 + element.load_week

            if not element.thursday_id:
                None
            else:
                element.load_week = element.thursday_id.load_task0 + element.thursday_id.load_task1 + element.thursday_id.load_task2 + element.thursday_id.load_task3 + element.load_week

            if not element.friday_id:
                None
            else:
                element.load_week = element.friday_id.load_task0 + element.friday_id.load_task1 + element.friday_id.load_task2 + element.friday_id.load_task3 + element.load_week

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


from odoo import fields, models

class EstateType(models.Model):
    _name="estate.property.type"
    _description="Type de propriete"

    name = fields.Char(required=True)
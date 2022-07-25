from soupsieve import select
from tomlkit import value
from traitlets import default
from odoo import fields, models

class Property(models.Model):
    _name = "estate.property"
    _description = "ESTATE proerty"

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    vendeur = fields.Many2one("res.users", string="Vendeur", default=lambda self: self.env.user, readonly=True)
    acheteur = fields.Char(required=True)
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Datetime.today("09/02/2022"))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Type',
        selection=[('nord', 'Nord'), ('sud', 'Sud'), ('est', 'Est'), ('ouest', 'Ouest')],
    )
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        string = 'State',
        default = 'nouveau',
        selection = [('nouveau', 'Nouveau'), ('offre reçue', 'Offre reçue'), ('offre acceptée', 'Offre acceptée'), ('vendue', 'Vendue'), ('annulée', 'Annulée')],
        required = True,
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Tag")
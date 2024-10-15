from odoo import models, fields


class VitiKlasa(models.Model):
    _name = 'schoolmanages.viti.klasa'
    _description = 'Year Class'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Viti', required=True, tracking=True)

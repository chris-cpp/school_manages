from odoo import models, fields

class VitiKlasa(models.Model):
    _name = 'schoolmanages.viti.klasa'
    _description = 'Year Class'

    name = fields.Char(string='Viti', required=True)
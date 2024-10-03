from odoo import models, fields

class Subject(models.Model):
    _name = 'schoolmanages.subject'
    _description = 'Subject'

    name = fields.Char(string='Lenda', required=True)
    subject_code = fields.Char(string='Kodi i lendees', required=True, unique=True)
    teacher_ids = fields.Many2many('schoolmanages.teacher', string='Mesuesi')
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti Klasa', required=True)  # Add this line
    active = fields.Boolean(string='Active', default=True)
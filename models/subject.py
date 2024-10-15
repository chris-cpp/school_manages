from odoo import models, fields

class Subject(models.Model):
    _name = 'schoolmanages.subject'
    _description = 'Subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Lenda', required=True, tracking=True)
    subject_code = fields.Char(string='Kodi i lendees', required=True, unique=True, tracking=True)
    teacher_ids = fields.Many2many('schoolmanages.teacher', string='Mesuesi', tracking=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti Klasa', required=True, tracking=True)  # Add this line
    active = fields.Boolean(string='Active', default=True, tracking=True)


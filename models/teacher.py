from odoo import models, fields


class Teacher(models.Model):
    _name = 'schoolmanages.teacher'
    _description = 'Teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Emri', required=True, tracking=True)
    teacher_nid = fields.Char(string='Nr personal', required=True, unique=True, tracking=True)
    subject_ids = fields.Many2many('schoolmanages.subject', string='Lenda', tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    address = fields.Char(string='Adresa', required=True, tracking=True)
    phone = fields.Char(string='Nr. Telefoni', tracking=True)
    salary = fields.Float(string='Paga', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    date_of_joining = fields.Date(string='Data e Fillimit', tracking=True)

    _sql_constraints = [
        ('unique_user',
         'UNIQUE(user_id)',
         'A user can only be linked to one teacher.')
    ]

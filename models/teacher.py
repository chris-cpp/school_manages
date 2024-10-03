from odoo import models, fields


class Teacher(models.Model):
    _name = 'schoolmanages.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Emri', required=True)
    teacher_nid = fields.Char(string='Nr personal', required=True, unique=True)
    subject_ids = fields.Many2many('schoolmanages.subject', string='Lenda')
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [
        ('unique_user',
         'UNIQUE(user_id)',
         'A user can only be linked to one teacher.')
    ]

from odoo import models, fields


class Teacher(models.Model):
    _name = 'schoolmanages.teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    teacher_id = fields.Char(string='Teacher ID', required=True, unique=True)
    subject_ids = fields.Many2many('schoolmanages.subject', string='Subjects')
    active = fields.Boolean(string='Active', default=True)

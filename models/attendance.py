from odoo import models, fields
from datetime import date


class Attendance(models.Model):
    _name = 'schoolmanages.attendance'
    _description = 'Attendance'
    _rec_name = 'student_id'

    student_id = fields.Many2one('schoolmanages.student', string='Student', required=True)
    date = fields.Date(string='Date', required=True, default=lambda self: fields.Date.context_today(self))
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string='Status', required=True)
    active = fields.Boolean(string='Active', default=True)
    teacher_id = fields.Many2one('schoolmanages.teacher', string='Mesuesi')

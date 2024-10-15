from odoo import models, fields
from datetime import date


class Attendance(models.Model):
    _name = 'schoolmanages.attendance'
    _description = 'Attendance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'

    student_id = fields.Many2one('schoolmanages.student', string='Student', required=True, tracking=True)
    date = fields.Date(string='Date', required=True, default=lambda self: fields.Date.context_today(self),
                       tracking=True)
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string='Status', tracking=True,
                              required=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    teacher_id = fields.Many2one('schoolmanages.teacher', string='Mesuesi', tracking=True)

    def action_present(self):
        self.status = 'present'

    def action_absent(self):
        self.status = 'absent'

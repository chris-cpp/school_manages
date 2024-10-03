from odoo import models, fields

class AttendanceReportWizard(models.TransientModel):
    _name = 'attendance.report.wizard'
    _description = 'Attendance Report Wizard'

    start_date = fields.Date(string='Date Fillimi')
    end_date = fields.Date(string='Date Mbarimi')
    student_id = fields.Many2one('schoolmanages.student', string='Student')

    def action_generate_report(self):
        self.ensure_one()
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'student_id': self.student_id.id if self.student_id else None,
        }
        return self.env.ref('schoolmanages.action_report_attendance').report_action(None, data=data)
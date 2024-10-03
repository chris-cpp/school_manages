from odoo import models, fields

class StudentGradeReportWizard(models.TransientModel):
    _name = 'student.grade.report.wizard'
    _description = 'Student Grade Report Wizard'

    student_id = fields.Many2one('schoolmanages.student', string='Student', required=True)
    academic_year_id = fields.Many2one('schoolmanages.academic.year', string='Academic year')
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa',string='Viti')


    def action_generate_report(self):
        self.ensure_one()
        data = {
            "student_id": self.student_id.id,
            "academic_year_id": self.academic_year_id.id if self.academic_year_id else None,
            "viti_klasa_id": self.viti_klasa_id.id if self.viti_klasa_id else None,
        }
        return self.env.ref('schoolmanages.action_report_student_grade').report_action(None,data=data)

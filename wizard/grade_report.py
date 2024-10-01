from odoo import fields, models

class GradeReport(models.TransientModel):
    _name = 'grade.report'
    _description = 'Grade'

    student_id = fields.Many2one(comodel_name='schoolmanages.student', string='Products')
    subject_id = fields.Many2one(comodel_name='schoolmanages.subject', string='Subjects')
    class_id = fields.Many2one(comodel_name='schoolmanages.class', string='Products')
    viti_akademik_id = fields.Many2one(comodel_name='schoolmanages.academic.year', string='Products')
    # start_date = fields.Date(default=fields.Datetime.now, string='Start date', required=True)
    # end_date = fields.Date(default=fields.Datetime.now, string='End date', required=True)

    def print_report(self):
        self.ensure_one()
        data = {
            "student_id": self.student_id.id,
            "subject_id": self.subject_id,
            "class_ids": self.class_id,
            "viti_akademik_id": self.viti_akademik_id,
            # "end_date": self.end_date,
        }
        return self.env.ref('schoolmanages.action_report_grade').report_action(None, data=data)

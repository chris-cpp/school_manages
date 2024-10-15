from odoo import fields, models


class InvoiceReport(models.TransientModel):
    _name = 'student.report'
    _description = 'Student Report'

    student_ids = fields.Many2one(comodel_name='schoolmanages.student', string='Studenti')
    status = fields.Selection(
        [('kalues', 'Kalues'), ('ngeles', 'Ngeles'), ('diplomuar', 'Diplomuar'), ('regjistruar', 'Regjistruar'),('ne progres','Ne progres')],
        string='Status')

    # start_date = fields.Date(default=fields.Datetime.now, string='Start date', required=True)
    # end_date = fields.Date(default=fields.Datetime.now, string='End date', required=True)

    def print_report(self):
        self.ensure_one()
        data = {
            "student_ids": self.student_ids.ids,
            "status": self.status,
            # "end_date": self.end_date,
        }
        return self.env.ref('schoolmanages.action_report_student').report_action(None, data=data)


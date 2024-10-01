from odoo import models, api


class SchoolmanageReportStudent(models.AbstractModel):
    _name = 'report.schoolmanages.report_student'
    _description = 'Student Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        student_ids = data.get('student_ids')  # Replace with the actual key for student ID if needed
        student_name = data.get('student_name')  # Replace with the actual key for student name if needed
        student_status = data.get('status')
        # Initialize an empty domain list
        domain = []

        # Add a condition to filter by student ID if it is provided
        if student_ids:
            domain.append(('id', '=', student_ids))  # Assuming 'id' is the field name for student ID
        if student_name:
            domain.append(('name', 'ilike', student_name))  # Using 'ilike' for case-insensitive match
        if student_status:
            domain.append(('status', '=', student_status))

        # Search for students with the specified ID and/or name
        student_obj = self.env['schoolmanages.student'].search(domain)

        res = {}

        for student in student_obj:
            student_id = student.id
            if student_id not in res:
                res[student_id] = {
                    'name': student.name,
                    'nr_amzes': student.nr_amzes,
                    'birth_date': student.birth_date,
                    'status': student.status,
                }

        return {
            'docs': res.values(),
            'r_name' : 'Lista e studenteve',
        }

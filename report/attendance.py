from odoo import models, api


class SchoolmanageReportAttendance(models.AbstractModel):
    _name = 'report.schoolmanages.report_attendance'
    _description = 'Attendance Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Retrieve the attendance records based on the data passed from the wizard
        student_ids = data.get('student_id', [])
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # Prepare the domain for fetching attendance records
        domain = []
        if student_ids:
            domain.append(('student_id', 'in', student_ids))
        if start_date:
            domain.append(('date', '>=', start_date))
        if end_date:
            domain.append(('date', '<=', end_date))

        # Fetch attendance records
        attendance_records = self.env['schoolmanages.attendance'].search(domain)

        # Prepare data for the report
        report_data = []
        for attendance in attendance_records:
            report_data.append({
                'student_name': attendance.student_id.name,
                'date': attendance.date,
                'status': attendance.status,
                'teacher_name': attendance.teacher_id.name if attendance.teacher_id else 'N/A',
            })

        print(report_data)

        return {
            'docs': report_data,
            'r_name': ', '.join(set(record['student_name'] for record in report_data)),  # Unique student names
        }
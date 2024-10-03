from odoo import models, api


class SchoolmanageReportGrade(models.AbstractModel):
    _name = 'report.schoolmanages.report_grade'
    _description = 'Grade Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Retrieve the grades based on the student IDs passed
        student_ids = data.get('student_id', [])
        if isinstance(student_ids, int):  # Check if a single integer is passed
            student_ids = [student_ids]  # Convert to a list
        grades = self.env['schoolmanages.grade'].search([('student_id', 'in', student_ids)])
        distinct_subjects = set()
        print(grades)
        period_mapping = {
            'T1': 'Tremujori i I',
            'T2': 'Tremujori i II',
            'T3': 'Tremujori i III'
        }

        if student_ids:
            # Fetch the student records based on the IDs
            students = self.env['schoolmanages.student'].search_read([
                ('id', 'in', student_ids)
            ], fields=['id', 'name'])  # Assuming 'name' is the field for the student's name
            # Extract names from the fetched records
            student_names = [student['name'] for student in students]
            formatted_student_names = ', '.join(student_names)

            student_report=[formatted_student_names]


        else:
            student_names = []  # Empty list if no student IDs are provided
            formatted_student_names = ', '.join(student_names)


        # Prepare data for the report
        report_data = []
        for grade in grades:
            student_name = grade.student_id.name
            if student_name not in distinct_subjects:
                distinct_subjects.add(student_name)
            report_data.append({
                'student_name': grade.student_id.name,  # Accessing the student's name
                'subject_name': grade.subject_id.name,   # Ensure you reference the subject's name
                'academic_year': grade.academic_year_id.name,
                'nota_vazhduar' : grade.note_vazhduar,
                'nota_provim' : grade.note_provim,
                'nota_projekt' : grade.note_projekt,
                'total_grade': grade.nota_totale,
                'periudha': period_mapping.get(grade.periudha, grade.periudha),
            })


        print(report_data)
        return {
            'docs': report_data,
            'r_name': student_report,
        }
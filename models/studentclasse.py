from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StudentClassConnection(models.Model):
    _name = 'schoolmanages.student.class.connection'
    _description = 'Student Class Connection'
    _rec_name = 'student_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Many2one('schoolmanages.student', string='Student', required=True, tracking=True)
    class_id = fields.Many2one('schoolmanages.class', string='Klasa', required=True, tracking=True)
    academic_year_id = fields.Many2one('schoolmanages.academic.year', string='Viti akademik', required=True, tracking=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa',string='Viti Klasa', required=True, tracking=True)

    # Optional: Add a constraint to ensure a student can only be enrolled in a class for a specific academic year
    _sql_constraints = [
        ('unique_student_academic_year',
         'UNIQUE(student_id, academic_year_id)',
         'A student cannot be enrolled in more than one class for the same academic year.'),
        ('unique_student_class_academic_year',
         'UNIQUE(student_id, class_id, academic_year_id)',
         'A student cannot be enrolled in the same class for the same academic year more than once.')
    ]


    # Add a constraint to ensure the class doesn't exceed 30 students per academic year
    @api.constrains('class_id', 'academic_year_id')
    def _check_class_student_limit(self):
        for record in self:
            # Count the number of students in the same class for the given academic year
            student_count = self.env['schoolmanages.student.class.connection'].search_count([
                ('class_id', '=', record.class_id.id),
                ('academic_year_id', '=', record.academic_year_id.id)
            ])

            if student_count >= 30:
                raise ValidationError(f'The class {record.class_id.name} already has 30 students for the academic year {record.academic_year_id.name}. You cannot add more students.')

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            self.viti_klasa_id = self.class_id.viti_klasa_id  # Automatically fill viti_klasa_id
        else:
            self.viti_klasa_id = False  # Clear the field if no class is selected


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolClass(models.Model):
    _name = 'schoolmanages.class'
    _description = 'Class'

    name = fields.Char(string='Class Name', required=True)
    teacher_id = fields.Many2one('schoolmanages.teacher', string='Class Teacher')
    # student_ids = fields.Many2many('schoolmanages.student',
    #                                 'student_class_rel',
    #                                 'class_id',
    #                                 'student_id',
    #                                 string='Students')
    # connection_ids = fields.One2many('schoolmanages.student.class.connection', 'class_id', string='Student Connections')
    active = fields.Boolean(string='Active', default=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti Klasa', required=True)  # Add this line

    @api.constrains('student_ids')
    def _check_student_limit(self):
        for classroom in self:
            if len(classroom.student_ids) >= 30:
                raise ValidationError("The number of students in the classroom cannot exceed 30.")

    @api.constrains('teacher_id')
    def _check_teacher_limit(self):
        for classroom in self:
            if classroom.teacher_id:
                other_classes = self.search([('teacher_id', '=', classroom.teacher_id.id), ('id', '!=', classroom.id)])
                if other_classes:
                    raise ValidationError(
                        f"The teacher '{classroom.teacher_id.name}' is already assigned to another class.")

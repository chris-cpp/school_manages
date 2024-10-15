from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolClass(models.Model):
    _name = 'schoolmanages.class'
    _description = 'Class'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Klasa', required=True, tracking=True)
    teacher_id = fields.Many2one('schoolmanages.teacher', string='Class Teacher', tracking=True)
    # student_ids = fields.Many2many('schoolmanages.student',
    #                                 'student_class_rel',
    #                                 'class_id',
    #                                 'student_id',
    #                                 string='Students')
    # connection_ids = fields.One2many('schoolmanages.student.class.connection', 'class_id', string='Student Connections')
    active = fields.Boolean(string='Active', default=True, tracking=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti Klasa', tracking=True, required=True)  # Add this line

    @api.constrains('student_ids')
    def _check_student_limit(self):
        for classroom in self:
            if len(classroom.student_ids) >= 30:
                raise ValidationError("Nje klase mund te kete deri ne 30 nxenes.")

    @api.constrains('teacher_id')
    def _check_teacher_limit(self):
        for classroom in self:
            if classroom.teacher_id:
                other_classes = self.search([('teacher_id', '=', classroom.teacher_id.id), ('id', '!=', classroom.id)])
                if other_classes:
                    raise ValidationError(
                        f"Mesuesi '{classroom.teacher_id.name}' eshte i lidhur me nje klase tjeter.")

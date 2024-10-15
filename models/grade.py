from odoo import models, fields, api
from datetime import date

from odoo.exceptions import ValidationError


class Grade(models.Model):
    _name = 'schoolmanages.grade'
    _description = 'Grade'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_id'

    student_id = fields.Many2one('schoolmanages.student', string='Student', tracking=True, required=True)
    subject_id = fields.Many2one('schoolmanages.subject', string='Lenda', tracking=True)
    note_vazhduar = fields.Integer(string='Note Vazhduar', tracking=True)
    note_provim = fields.Integer(string='Note Provim', tracking=True)
    note_projekt = fields.Integer(string='Note Projekt', tracking=True)
    nota_totale = fields.Float(string='Nota', compute='_compute_totale', store=True, tracking=True)
    # date = fields.date.today()
    periudha = fields.Selection([
        ('T1', 'Tremujori i I'),
        ('T2', 'Tremujori i II'),
        ('T3', 'Tremujori i III')
    ], string='Periudha', compute='_compute_periudha', tracking=True, store=True)
    academic_year_id = fields.Many2one('schoolmanages.academic.year', compute='_compute_academic_year',
                                       string='Viti Akademik', store=True, tracking=True)
    active = fields.Boolean(string='Active', default=True)
    class_id = fields.Many2one('schoolmanages.class', string='Klasa', tracking=True, store=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti Klasa', tracking=True, store=True)

    @api.depends('note_vazhduar', 'note_provim', 'note_projekt')
    def _compute_totale(self):
        for record in self:
            # Calculate the total grade based on the individual grades
            record.nota_totale = (
                    (record.note_vazhduar * 0.4) +
                    (record.note_provim * 0.4) +
                    (record.note_projekt * 0.2)
            )

    @api.depends('student_id')
    def _compute_periudha(self):
        for record in self:
            current_date = fields.Date.today()
            month = current_date.month
            if 9 <= month <= 12:
                record.periudha = 'T1'  # Tremujori i I
            elif 1 <= month <= 3:
                record.periudha = 'T2'  # Tremujori i II
            elif 4 <= month <= 6:
                record.periudha = 'T3'  # Tremujori i III
            else:
                record.periudha = 'Out of range'

    @api.depends('student_id')
    def _compute_academic_year(self):
        current_date = date.today()
        AcademicYear = self.env['schoolmanages.academic.year']
        for record in self:
            academic_year = AcademicYear.search([
                ('start_date', '<=', current_date),
                ('end_date', '>=', current_date),
                ('status', '=', 'aktiv')
            ], limit=1)
            record.academic_year_id = academic_year

    @api.onchange('student_id', 'academic_year_id')
    def _onchange_student_id(self):
        if self.student_id and self.academic_year_id:
            connection = self.env['schoolmanages.student.class.connection'].search([
                ('student_id', '=', self.student_id.id),
                ('academic_year_id', '=', self.academic_year_id.id)
            ], limit=1)

            if connection:
                self.class_id = connection.class_id.id
            else:
                self.class_id = False
                return {
                    'warning': {
                        'title': "No Class Found",
                        'message': "This student is not enrolled in any class for the selected academic year."
                    }
                }
        else:
            self.class_id = False

    @api.constrains('note_vazhduar', 'note_provim', 'note_projekt')
    def _check_nota_range(self):
        for record in self:
            if record.note_vazhduar < 4 or record.note_vazhduar > 10:
                raise ValidationError("Note Vazhduar duhet te jete ndermjet 4 and 10.")
            if record.note_provim < 4 or record.note_provim > 10:
                raise ValidationError("Note Provim duhet te jete ndermjet 4 and 10.")
            if record.note_projekt < 4 or record.note_projekt > 10:
                raise ValidationError("Note Projekt duhet te jete ndermjet  4 and 10.")

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            viti_klasa_id = self.class_id.viti_klasa_id
            self.viti_klasa_id = viti_klasa_id.id
            if viti_klasa_id:
                return {
                    'domain': {
                        'subject_id': [('viti_klasa_id', 'in', viti_klasa_id.id)]
                    }
                }
            else:
                self.subject_id = False
                return {
                    'domain': {
                        'subject_id': []
                    }
                }
        else:
            self.subject_id = False
            self.viti_klasa_id = False
            return {
                'domain': {
                    'subject_id': []
                }
            }

    @api.onchange('class_id')
    def _onchange_class_id_subject(self):
        if self.class_id:
            self.viti_klasa_id = self.class_id.viti_klasa_id.id
            return {
                'domain': {
                    'subject_id': [('viti_klasa_id', '=', self.viti_klasa_id)]
                }
            }
        else:
            self.viti_klasa_id = False
            return {
                'domain': {
                    'subject_id': [('id', '=', False)]
                }
            }

    _sql_constraints = [
        ('unique_student_subject_academic_year',
         'UNIQUE(student_id, subject_id, academic_year_id)',
         'A student can only receive a grade once for each subject in a specific academic year.')
    ]

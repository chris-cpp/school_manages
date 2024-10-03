from odoo import models, fields,api
from odoo.exceptions import ValidationError
from datetime import date


class Student(models.Model):
    _name = 'schoolmanages.student'
    _description = 'Student'

    name = fields.Char(string='Emri', required=True)
    nr_amzes = fields.Char(string='Nr Amzes', required=True, unique=True)
    birth_date = fields.Date(string='Ditelindja')
    # connection_ids = fields.One2many('schoolmanages.student.class.connection', 'student_id', string='Class Connections')
    address = fields.Char(string='Adresa', required=True)
    status = fields.Selection([('kalues', 'Kalues'), ('ngeles', 'Ngeles'),('diplomuar', 'Diplomuar'),('regjistruar','Regjistruar')],string='Status')



    # @api.constrains('class_ids')
    # def _check_classroom_student_limit(self):
    #     for student in self:
    #         if student.class_ids and len(student.class_ids.student_ids) >= 30:
    #             raise ValidationError("The classroom already has 30 students. Cannot add more.")


    @api.constrains('birth_date')
    def _check_age(self):
        for student in self:
            if student.birth_date:
                age = date.today().year - student.birth_date.year
                if (date.today().month, date.today().day) < (student.birth_date.month, student.birth_date.day):
                    age -= 1  # Adjust for birthday not yet occurred this year
                if age < 14:
                    raise ValidationError("Studenti duhet te jete mbi 14 vjec.")



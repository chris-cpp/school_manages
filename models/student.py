from odoo import models, fields,api


class Student(models.Model):
    _name = 'schoolmanages.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Emri', required=True, tracking=True)
    nr_amzes = fields.Char(string='Nr Amzes', required=True, unique=True, tracking=True)
    birth_date = fields.Date(string='Ditelindja', tracking=True)
    parent_id = fields.Many2one(comodel_name='schoolmanages.prinderit', string='Prindi')
    address = fields.Char(string='Adresa', required=True, tracking=True)
    phone = fields.Char(string='Nr. Telefoni', tracking=True)
    country = fields.Char(string='Shteti', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gjinia', tracking=True)
    status = fields.Selection([('regjistruar','Regjistruar'),('kalues', 'Kalues'), ('ngeles', 'Ngeles'),('ne progres','Ne progres'),('diplomuar', 'Diplomuar')],string='Status', tracking=True)




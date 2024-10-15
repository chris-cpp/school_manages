from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class AcademicYear(models.Model):
    _name = 'schoolmanages.academic.year'
    _description = 'Academic Year'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Viti Akademik', required=True, tracking=True)
    start_date = fields.Date(string='Date Fillimi', required=True, tracking=True)
    end_date = fields.Date(string='Date Mbarimi', required=True, tracking=True)
    status = fields.Selection([('aktiv','Aktiv'),('jo aktiv','Jo aktiv')], tracking=True)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date >= record.end_date:
                raise ValidationError("Data e fillimit duhet te jete me e madhe se data e mbarimit.")

    @api.model
    def update_academic_year_status(self):
        today = date.today()
        academic_years = self.search([('end_date', '<=', today)])
        for year in academic_years:
            year.status = 'jo aktiv'
        academic_years = self.search([('start_date', '>=',today)])
        for year in academic_years:
            year.status = 'aktiv'

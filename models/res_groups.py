from odoo import models, fields

class ResGroups(models.Model):
    _inherit = 'res.groups'

    teacher_group = fields.Boolean(string='Teacher Group', default=False)
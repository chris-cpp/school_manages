from odoo import models, fields, api


class ClassSubject(models.Model):
    _name = 'schoolmanages.class.subject'
    _description = 'Class Subject'

    class_id = fields.Many2one('schoolmanages.class', string='Klasa', required=True)
    subject_id = fields.Many2one('schoolmanages.subject', string='Lenda', required=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti')

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if self.class_id:
            self.viti_klasa_id = self.class_id.viti_klasa_id
        else:
            self.viti_klasa_id = False


    _sql_constraints = [
        ('unique_class_subject',
         'UNIQUE(class_id, subject_id)',
         'A subject can only be assigned to one class.')
    ]
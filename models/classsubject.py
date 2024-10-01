from odoo import models, fields, api


class ClassSubject(models.Model):
    _name = 'schoolmanages.class.subject'
    _description = 'Class Subject'

    class_id = fields.Many2one('schoolmanages.class', string='Class', required=True)
    subject_id = fields.Many2one('schoolmanages.subject', string='Subject', required=True)
    viti_klasa_id = fields.Many2one('schoolmanages.viti.klasa', string='Viti')

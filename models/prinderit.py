from odoo import fields, models, api
from odoo.exceptions import ValidationError
import urllib.parse


class Prinderit(models.Model):
    _name = 'schoolmanages.prinderit'
    _description = 'Prinderit'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Emri', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Telefon')
    student_ids = fields.One2many('schoolmanages.student', 'parent_id', string='Femija')
    address = fields.Char(string='Adresa')

    def action_share_whatsapp(self):
        if not self.phone:
            raise ValidationError("Missing phone number in prinderit record")
        message = 'Hi %s, we would like to inform you that an important event is coming up for your child at school.' % self.name
        encoded_message = urllib.parse.quote(message)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, encoded_message)
        self.message_post(body=message, subject="WhatsApp Message")
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }

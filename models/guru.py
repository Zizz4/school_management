from odoo import fields, models, api


class SchoolGuru(models.Model):
    _inherit = 'res.users'

    is_guru = fields.Boolean(string="Guru")
    age = fields.Integer(string="Umur")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")
    pelajaran_id = fields.Many2many(string='Pelajaran', comodel_name='school.pelajaran')
